#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import collections
import csv
import datetime as dt
import os
import random
import re
import sys
from typing import List, Dict, Any, Tuple

import feedparser
import yaml
import pandas as pd

# ---------------------------
# 基础：加载/保存 YAML
# ---------------------------
def load_pool(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Exploration pool YAML not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def save_pool(pool: Dict[str, Any], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(pool, f, sort_keys=False, allow_unicode=True)

# ---------------------------
# 抓取并标准化 RSS
# ---------------------------
def fetch_feed(url: str) -> List[Dict[str, Any]]:
    feed = feedparser.parse(url)
    entries = []
    for e in feed.entries:
        # arXiv 的唯一标识优先用 id/guid，否则回退 link/title 组合
        uid = getattr(e, "id", None) or getattr(e, "guid", None) or getattr(e, "link", None) or getattr(e, "title", "")
        entries.append({
            "id": uid,
            "title": getattr(e, "title", "").strip(),
            "link": getattr(e, "link", "").strip(),
            "published": getattr(e, "published", ""),
            "summary": getattr(e, "summary", "").strip(),
        })
    return entries

# ---------------------------
# 工具：文本匹配与清洗
# ---------------------------
def any_keyword_in(text: str, keywords: List[str]) -> bool:
    t = text.lower()
    return any(kw.lower() in t for kw in keywords)

def matches_topic(entry: Dict[str, Any], topic: Dict[str, Any]) -> bool:
    kws = topic.get("keywords", [])
    blob = f"{entry['title']} || {entry['summary']}"
    return any_keyword_in(blob, kws)

def matches_ignore(entry: Dict[str, Any], ignore_keywords: List[str]) -> bool:
    if not ignore_keywords:
        return False
    blob = f"{entry['title']} || {entry['summary']}".lower()
    return any(kw.lower() in blob for kw in ignore_keywords)

# ---------------------------
# 选择逻辑
# ---------------------------
def select_global(entries: List[Dict[str, Any]], seen: set, k: int, ignore_keywords: List[str], rng: random.Random) -> List[Dict[str, Any]]:
    pool = [e for e in entries if e["id"] not in seen and not matches_ignore(e, ignore_keywords)]
    if not pool:
        return []
    k = min(k, len(pool))
    return rng.sample(pool, k)

def weighted_choice(topics: List[Dict[str, Any]], rng: random.Random) -> Dict[str, Any]:
    weights = [float(t.get("weight", 1.0)) for t in topics]
    total = sum(weights) or 1.0
    probs = [w / total for w in weights]
    # 累积分布采样
    r = rng.random()
    c = 0.0
    for t, p in zip(topics, probs):
        c += p
        if r <= c:
            return t
    return topics[-1]

def select_from_pool(entries: List[Dict[str, Any]], pool_cfg: Dict[str, Any], seen: set, k: int, rng: random.Random, max_per_topic: int) -> List[Dict[str, Any]]:
    topics = pool_cfg.get("topics", []) or []
    ignore_keywords = pool_cfg.get("ignore_keywords", []) or []
    if not topics:
        return []

    selected = []
    attempts = 0
    # 防止死循环：尝试若干次抽满 k
    while len(selected) < k and attempts < k * 10:
        attempts += 1
        topic = weighted_choice(topics, rng)
        # 主题内匹配
        candidates = [e for e in entries
                      if e["id"] not in {x["id"] for x in selected}
                      and e["id"] not in seen
                      and matches_topic(e, topic)
                      and not matches_ignore(e, ignore_keywords)]
        if not candidates:
            continue
        # 控制单主题最大抽取数
        quota = min(max_per_topic, k - len(selected))
        take = min(quota, len(candidates))
        picked = rng.sample(candidates, take)
        selected.extend(picked)
    return selected[:k]

# ---------------------------
# 动态扩建：从标题中挖掘候选词/短语
# ---------------------------
STOPWORDS = set("""
a an the and or of for to from with on in by as into onto over under toward against
is are was were be been being this that these those it its their his her your our
via using beyond among between within without through across per each all any some
new fast robust efficient improved improved- a1 b2 c3 method approach framework
""".split())

def tokenize(s: str) -> List[str]:
    s = re.sub(r"[\(\)\[\]\{\}:;,\.\?\!/\|\"'`~\-+_=<>]", " ", s.lower())
    toks = [t for t in s.split() if t.isalpha()]
    return toks

def extract_ngrams(titles: List[str], min_len: int = 4) -> Tuple[List[str], List[str]]:
    # 1-gram
    uni_counter = collections.Counter()
    # 2-gram（连续词）
    bi_counter = collections.Counter()

    for title in titles:
        toks = tokenize(title)
        toks = [t for t in toks if t not in STOPWORDS and len(t) >= min_len]
        uni_counter.update(toks)
        for i in range(len(toks) - 1):
            bi = f"{toks[i]} {toks[i+1]}"
            bi_counter[bi] += 1

    unigrams = [w for w, _ in uni_counter.most_common()]
    bigrams = [w for w, _ in bi_counter.most_common()]
    return unigrams, bigrams

def propose_candidates(entries: List[Dict[str, Any]], pool_cfg: Dict[str, Any], top_uni: int, top_bi: int, min_len: int) -> List[str]:
    titles = [e["title"] for e in entries]
    unigrams, bigrams = extract_ngrams(titles, min_len=min_len)

    # 过滤已存在的关键词
    existing = set()
    for t in pool_cfg.get("topics", []):
        for kw in t.get("keywords", []):
            existing.add(kw.lower())

    proposals = []
    for w in unigrams[:top_uni]:
        if w.lower() not in existing:
            proposals.append(w)
    for w in bigrams[:top_bi]:
        if w.lower() not in existing:
            proposals.append(w)

    # 去重保序
    seen = set()
    uniq = []
    for p in proposals:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq

# ---------------------------
# 导出、日志与去重历史
# ---------------------------
def export_selection(selections: List[Dict[str, Any]], out_prefix: str, as_excel: bool = True, command: str = "") -> str:
    if not selections:
        return ""
    os.makedirs("outputs", exist_ok=True)
    df = pd.DataFrame(selections)

    # 在 DataFrame 中加一列，记录命令
    df["command"] = command

    date_str = dt.date.today().isoformat()
    if as_excel:
        path = os.path.join("outputs", f"{out_prefix}_{date_str}.xlsx")
        df.to_excel(path, index=False)
    else:
        path = os.path.join("outputs", f"{out_prefix}_{date_str}.csv")
        df.to_csv(path, index=False, encoding="utf-8-sig")
    return path

def append_log(selections: List[Dict[str, Any]], log_path: str = "reading_log.csv") -> None:
    header = ["date", "id", "title", "link", "published"]
    is_new = not os.path.exists(log_path)
    with open(log_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(header)
        for e in selections:
            writer.writerow([dt.date.today().isoformat(), e["id"], e["title"], e["link"], e["published"]])

def update_seen(pool: Dict[str, Any], selections: List[Dict[str, Any]]) -> None:
    seen = set(pool.get("history", {}).get("seen_ids", []))
    for e in selections:
        seen.add(e["id"])
    pool.setdefault("history", {})["seen_ids"] = sorted(list(seen))

# ---------------------------
# 主流程
# ---------------------------
def main():
    parser = argparse.ArgumentParser(description="arXiv RSS picker: global / pool / expand / mixed")
    parser.add_argument("--pool", type=str, default="exploration_pool.yaml", help="Path to exploration pool YAML")
    parser.add_argument("--mode", type=str, default="mixed", choices=["global", "pool", "expand", "mixed"], help="Selection mode")
    parser.add_argument("--feed", type=str, default=None, help="Override feed URL")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (for reproducibility)")
    parser.add_argument("--global-k", type=int, default=None, help="Override global random pick count")
    parser.add_argument("--pool-k", type=int, default=None, help="Override pool random pick count")
    parser.add_argument("--max-per-topic", type=int, default=None, help="Override max per topic in pool mode")
    parser.add_argument("--excel", action="store_true", help="Export .xlsx instead of .csv")
    args = parser.parse_args()

    rng = random.Random(args.seed)

    pool_cfg = load_pool(args.pool)
    settings = pool_cfg.get("settings", {})
    feed_url = args.feed or settings.get("feed_url", "https://export.arxiv.org/rss/cs.CV")
    ignore_keywords = pool_cfg.get("pool", {}).get("ignore_keywords") or pool_cfg.get("ignore_keywords") or []
    # 兼容 YAML 顶层 pool/ settings 结构
    pool_block = pool_cfg.get("pool", pool_cfg)

    daily = settings.get("daily_pick", {})
    global_k = args.global_k if args.global_k is not None else daily.get("global_count", 4)
    pool_k = args.pool_k if args.pool_k is not None else daily.get("pool_count", 3)
    max_per_topic = args.max_per_topic if args.max_per_topic is not None else daily.get("max_per_topic", 2)

    autosuggest = settings.get("autosuggest", {})
    top_uni = int(autosuggest.get("top_unigrams", 15))
    top_bi = int(autosuggest.get("top_bigrams", 10))
    min_len = int(autosuggest.get("min_len", 4))

    entries = fetch_feed(feed_url)

    # 历史去重集
    seen_ids = set(pool_cfg.get("history", {}).get("seen_ids", []))

    selections = []

    if args.mode == "global":
        selections = select_global(entries, seen_ids, global_k, ignore_keywords, rng)

    elif args.mode == "pool":
        selections = select_from_pool(entries, pool_block, seen_ids, pool_k, rng, max_per_topic)

    elif args.mode == "mixed":
        part_global = max(0, global_k)
        part_pool = max(0, pool_k)
        sel_g = select_global(entries, seen_ids, part_global, ignore_keywords, rng)
        # 更新 seen 临时集合以避免 pool 再抽到相同
        tmp_seen = seen_ids.union({e["id"] for e in sel_g})
        sel_p = select_from_pool(entries, pool_block, tmp_seen, part_pool, rng, max_per_topic)
        selections = sel_g + sel_p

    elif args.mode == "expand":
        proposals = propose_candidates(entries, pool_block, top_uni, top_bi, min_len)
        # 合并进 candidates（去重保序）
        old = pool_block.get("candidates", [])
        merged = list(dict.fromkeys(old + proposals))
        pool_block["candidates"] = merged
        pool_cfg["pool"] = pool_block
        save_pool(pool_cfg, args.pool)
        print(f"[expand] Proposed {len(proposals)} candidates. Pool updated at: {args.pool}")
        # 也导出一个候选 CSV 供你人工浏览
        os.makedirs("outputs", exist_ok=True)
        cand_path = os.path.join("outputs", f"candidates_{dt.date.today().isoformat()}.csv")
        pd.DataFrame({"candidate": proposals}).to_csv(cand_path, index=False, encoding="utf-8-sig")
        print(f"[expand] Candidates CSV saved to: {cand_path}")
        return

    # 输出与日志
    if selections:
        # 基本去重
        selections_unique = []
        seen_tmp = set()
        for e in selections:
            if e["id"] not in seen_tmp:
                seen_tmp.add(e["id"])
                selections_unique.append(e)
        selections = selections_unique

        # 导出
        prefix = f"selection_{args.mode}"
        out_path = export_selection(selections, prefix, as_excel=args.excel)
        if out_path:
            print(f"[ok] Selection saved to: {out_path}")

        # 记录日志
        append_log(selections, "reading_log.csv")
        print(f"[ok] Appended {len(selections)} items to reading_log.csv")

        # 更新历史 seen
        update_seen(pool_cfg, selections)
        save_pool(pool_cfg, args.pool)
        print(f"[ok] Exploration pool updated: {args.pool}")
    else:
        print("[warn] No items selected. Consider relaxing filters or increasing K.")

    
    cmd_str = " ".join(sys.argv)
    out_path = export_selection(selections, prefix, as_excel=args.excel, command=cmd_str)

if __name__ == "__main__":
    main()