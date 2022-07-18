# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 上午 10:58
# @Author : fengzhanwei
# @File : 常见的异常类型.py
# @Software : PyCharm

# （1）数学运算异常
# print(10/0)#ZeroDivisionError

lst=[11,22,33,44]
# print(lst[4]) #IndexError 索引从0开始

dic={'name':'张三','age':'20'}
# print(dic['gender']) #KeyError 没有叫做gender的键

# print(num) #NameError

# int a=10 #SyntaxError

# a=int('hello') #ValueError