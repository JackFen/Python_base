# -*- codeing = utf-8 -*-
# @Time : 2022-07-21 下午 3:13
# @Author : fengzhanwei
# @File : 文件的写.py
# @Software : PyCharm

# file=open('b.txt','w',encoding='UTF-8') #覆盖原文件内容
file=open('b.txt','a',encoding='UTF-8') #在原文件上追加内容
file.write('Python')
file.close()