# -*- codeing = utf-8 -*-
# @Time : 2022-07-21 下午 3:13
# @Author : fengzhanwei
# @File : 文件的读取.py
# @Software : PyCharm
file=open('a.txt','r',encoding='UTF-8')
print(file.readlines()) #结果是一个列表
file.close()