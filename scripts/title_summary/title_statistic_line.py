import pandas as pd
import argparse
import os
import chardet

def count_fellows_and_members(csv_file, output_file=None):
    """
    统计CSV文件中作者的Fellow和院士信息. 若作者为院士, 则院士数量加一, 若作者为 IEEE Fellow, ACM Fellow或IEEE Life Fellow则Fellow数量加一. 其输入文件格式请见同目录下的 1.csv 文件, 需要进行格式统一(如删除空格, 但不要求数据顺序)
    
    参数:
    csv_file: 输入的CSV文件路径
    output_file: 输出结果的文件路径(可选)
    """

    with open(csv_file, 'rb') as f:
        raw = f.read(2000)
        res = chardet.detect(raw)
        file_encoding = res['encoding']
        print(f'检测到文件编码为: {file_encoding}')
    
    try:
        # 读取CSV文件
        df = pd.read_csv(csv_file, encoding=file_encoding)  # 使用制表符分隔，如果实际是逗号分隔，请改为sep=','
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return
    
    # 初始化统计结果
    fellow_count = 0
    member_count = 0
    results = []
    
    print("开始处理数据...")
    
    # 遍历每一行
    for index, row in df.iterrows():
        is_fellow = False
        is_member = False
        
        # 检查所有头衔列
        for i in range(2, 7):  # 头衔1到头衔5，索引2到6
            col_name = f"title{i-1}"  # 构建列名
            title = str(row[col_name]) if pd.notna(row[col_name]) else ""
            
            # 检查是否为IEEE Fellow或ACM Fellow
            if "IEEE Fellow" in title or "ACM Fellow" in title or "IEEE Life Fellow" in title:
                is_fellow = True
            
            # 检查是否为院士
            if "院士" in title:
                is_member = True
        
        # 根据检查结果更新计数
        if is_fellow:
            fellow_count += 1
        if is_member:
            member_count += 1
        
        # 记录当前行的结果
        results.append({
            "统计序号": row["num"],
            "作者姓名": row["name"],
            "是否为Fellow": "是" if is_fellow else "否",
            "是否为院士": "是" if is_member else "否"
        })
    
    # 创建结果DataFrame
    result_df = pd.DataFrame(results)
    
    # 显示统计结果
    print("\n=== 统计结果 ===")
    print(f"Fellow人数: {fellow_count}")
    print(f"院士人数: {member_count}")
    
    # 显示前几行结果
    print("\n=== 前几行详细结果 ===")
    print(result_df.head())
    
    # 如果指定了输出文件，保存结果
    if output_file:
        try:
            result_df.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"\n结果已保存到: {output_file}")
        except Exception as e:
            print(f"保存文件时出错: {e}")
    
    return result_df, fellow_count, member_count

def main():
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='统计CSV文件中作者的Fellow和院士信息')
    parser.add_argument('input_file', help='输入的CSV文件路径')
    parser.add_argument('-o', '--output', help='输出结果的文件路径(可选)')
    
    # 解析参数
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"错误: 文件 '{args.input_file}' 不存在")
        return
    
    # 处理文件
    count_fellows_and_members(args.input_file, args.output)

if __name__ == "__main__":
    main()