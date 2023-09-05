# encoding=utf-8
import time
import os
"""
@xc
# 2021/12/21 20:45   文件汇总  修改2023/06/19 10:04
从某个目录下读取每个txt数据,并保存到同一个txt里
"""
# 初始路径，即需合并文件存放路径
path = r'E:\\users\\' 

dirs=os.listdir(path)   # 读取当前目录所有文件名
bpath = path+'respone2.txt'           # 文件名拼接，存放输出的文件
start = time.time()
print(bpath)
def merge():
    for file in dirs:
        # 读取 在a文档内容
        with open(path+file,'r',encoding='utf-8',errors='ignore') as f:    
            # 写入 到b文档内容    
            with open(bpath, 'a',encoding='utf-8') as s:           
                for i in f.readlines():
                    s.write(i)
                s.close()
                print('End')
        end = time.time()
        costtime = end - start
        print(costtime)
    print('endendendend')

merge()






















