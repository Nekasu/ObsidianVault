import pandas as pd
import chardet

def title_statistic_total(file_path):
    '''
    该函数接受一个 csv文件的路径作为输入, 统计其中头衔出现的次数. 仅统计出现的次数, 不考虑一人是否有多个头衔的情况.
    要求csv有同路径下1.csv的格式.
    输出一个同路径下output.csv的文件
    '''
    with open(file_path, 'rb') as f:
        raw = f.read(2000)
        res = chardet.detect(raw)
        file_encoding = res['encoding']
        print(f'检测到文件编码为: {file_encoding}')
    
    dp = pd.read_csv(file_path, encoding=file_encoding)
    
    i = -1
    d = {}
    for name in dp.head():
        dp[name] = dp[name].astype(str).fillna('')
        # print(name)
        i += 1
        if i <= 1:
            continue
        else: 
            for cell in dp[name]:
                cell = cell.upper()
                if cell == 'NAN':
                    continue
                elif cell not in d:
                    d[cell] = 1
                else:
                    d[cell] += 1
    
    print(d)
    df = pd.DataFrame(list(d.items()), columns=['Title', 'Count'])
    df.to_csv('output.csv', index=False, encoding=file_encoding)
    # for name in dp['title1']:
    #     print(name)

def name_summary(file_path):
    '''
    一个统计文档中出现了多少人名的程序.
    其格式要求如同目录下的1.csv所示
    输出结果在命令行中.
    '''
    with open(file_path, 'rb') as f:
        raw = f.read(2000)
        res = chardet.detect(raw)
        file_encoding = res['encoding']
        print(f'检测到文件编码为: {file_encoding}')
    
    dp = pd.read_csv(file_path, encoding=file_encoding)
 
    i = 0
    l = []
    for person in dp['name']:
        if person not in l:
            i += 1
            l.append(person)
            
            
    print(i)
title_statistic_total('1.csv')
name_summary('1.csv')