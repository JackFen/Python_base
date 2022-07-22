# -*- codeing = utf-8 -*-
# @Time : 2022-07-22 上午 11:42
# @Author : fengzhanwei
# @File : os中walk的使用.py
# @Software : PyCharm

import os
path=os.getcwd()
lst_files=os.walk(path) #返回一个元组,递归遍历
print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('-------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir)) #看当前目录下有多少个子目录
    for file in filename:
        print(os.path.join(dirpath,file))
    print('------------------')