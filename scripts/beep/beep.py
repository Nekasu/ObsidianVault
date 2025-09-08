'''
<span class="color-kachina-yellow">2025-06-19 14:34 周四.</span> 从 抖音 上刷到<a href=" https://v.douyin.com/Y4L0NqSBWzI/">一种专注学习的方法</a>, 我打算进行一段时间的实验, 下面我将介绍该方法. 首先介绍整体框架. 整体来说, 该方法要求专注 90 min 后休息 20 min. 其次介绍其中细节. 在 90 min 的专注过程中, 每隔 3~5 min 就播放一段提示音. 在听到提示音后, 我们就闭眼休息 10 s, 随后继续工作. <br>

为了实现该方法, 编写了程序 './scripts/beep.py'. 
'''
import time
import random
import threading
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play

LOG_FILE = "focus_log.txt"

def log_to_file(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {message}\n")

def load_sound(path):
    return AudioSegment.from_file(path)

def play_beep(sound):
    play(sound)

# 用于控制暂停和继续
pause_event = threading.Event()
pause_event.set()  # 初始为运行状态

# 非阻塞 sleep，允许中途暂停
def interruptible_sleep(seconds):
    for _ in range(int(seconds)):
        while not pause_event.is_set():
            time.sleep(0.1)  # 等待恢复
        time.sleep(1)

# 键盘监听线程
def keyboard_listener():
    while True:
        cmd = input().strip().lower()
        if cmd == "p":
            pause_event.clear()
            print(">>> 已暂停专注计时")
            log_to_file("用户暂停专注计时。")
        elif cmd == "r":
            if not pause_event.is_set():
                pause_event.set()
                print(">>> 已恢复专注计时")
                log_to_file("用户恢复专注计时。")

def focus_training(beep_file, bell_start_file, bell_end_file):
    print("开始专注训练（按 Ctrl+C 停止，输入 p 暂停 / r 恢复）\n")

    beep = load_sound(beep_file)
    bell_start = load_sound(bell_start_file)
    bell_end = load_sound(bell_end_file)

    cycle_count = 0
    total_focus_seconds = 0

    # 启动键盘监听线程
    threading.Thread(target=keyboard_listener, daemon=True).start()

    try:
        while True:
            cycle_count += 1
            print(f"第 {cycle_count} 轮专注开始：")
            log_to_file(f"开始第 {cycle_count} 轮专注。")

            start_time = time.time()
            elapsed = 0

            # ----------- 90分钟专注期 -----------
            while elapsed < 90 * 60:
                wait_time = random.randint(180, 300)
                time_remaining = 90 * 60 - elapsed
                if wait_time > time_remaining:
                    wait_time = time_remaining

                interruptible_sleep(wait_time)
                elapsed = time.time() - start_time

                if elapsed < 90 * 60:
                    play_beep(beep)
                    print("提示音响起，闭眼休息 10 秒...\n")
                    interruptible_sleep(10)

            total_focus_seconds += 90 * 60
            log_to_file(f"完成第 {cycle_count} 轮专注（90分钟）")

            # ----------- 20分钟休息期 -----------
            print("专注期结束，播放下课铃。")
            play_beep(bell_end)
            print("进入休息期（20分钟）...\n")
            log_to_file(f"完成第 {cycle_count} 轮休息（20分钟）")

            interruptible_sleep(20 * 60)

            print("播放上课铃，休息结束。\n")
            play_beep(bell_start)

    except KeyboardInterrupt:
        end_time = time.time()
        partial_focus = end_time - start_time
        if partial_focus < 90 * 60:
            total_focus_seconds += partial_focus
            log_to_file(f"第 {cycle_count} 轮未完成，中断，专注了 {int(partial_focus // 60)} 分钟。")
        print("\n训练已手动停止。\n")
        print(f"你共完成了 {cycle_count - 1} 个完整的 110 分钟周期。")
        print(f"累计专注时间为 {int(total_focus_seconds // 60)} 分钟。")

        log_to_file(f"累计完成 {cycle_count - 1} 个完整周期，总专注 {int(total_focus_seconds // 60)} 分钟。")
        log_to_file("本次训练结束。\n")

if __name__ == "__main__":
    beep_file = "beep.mp3"              # 每3~5min播放的提示音
    bell_start_file = "rest.wav"  # 上课铃（休息结束）
    bell_end_file = "rest.wav"      # 下课铃（进入休息）
    focus_training(beep_file, bell_start_file, bell_end_file)