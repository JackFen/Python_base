# -*- codeing = utf-8 -*-
# @Time : 2022-07-21 下午 4:01
# @Author : fengzhanwei
# @File : 文件对象的常用操作.py
# @Software : PyCharm

# file=open('a.txt','r',encoding='UTF-8')
# # print(file.read()) #读取文件的全部内容
# # print(file.read(2)) #读取 2 个字符
# # print(file.readline()) #读取一行
# print(file.readlines()) #按行读取文件，返回一个列表
# file.close()

# file=open('c.txt','a',encoding='UTF-8')
# lst=['java','go','python']
# file.writelines(lst)
# file.close()

# file=open('a.txt','r',encoding='UTF-8')
# file.seek(2)
# print(file.read())
# print(file.tell()) #位置从0开始计算
# file.close()

file=open('d.txt','a')
file.write('hello')
file.flush() #将缓冲区的内容写到文件中
file.write('world')
file.close()