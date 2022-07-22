# -*- codeing = utf-8 -*-
# @Time : 2022-07-22 上午 11:22
# @Author : fengzhanwei
# @File : os.path模块常用方法.py
# @Software : PyCharm

import os.path
# print(os.path.abspath('with语句.py')) #获取文件的绝对路径
# print(os.path.exists('with语句.py'),os.path.exists('demo18.py')) #判断文件或者目录是否存在
# print(os.path.join(r'E:\Python','demo16.py')) #对路径进行拼接
# print(os.path.split(r'E:\python\demo14.py')) #分离路径和文件名
# print(os.path.splitext('demo14.py')) #分离文件名和扩展名
# print(os.path.basename(r'E:\python\demo14.py')) #获取文件名
# print(os.path.dirname(r'E:\python\demo14.py')) #获取路径
# print(os.path.isdir(r'E:\python\demo14.py')) #判断是否为路径

# 列出指定目录下的所有py文件
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)