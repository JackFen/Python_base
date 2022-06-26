# -*- codeing = utf-8 -*-
# @Time : 2022/6/26 上午 1:35
# @Author : fengzhanwei
# @File : 字符串.py
# @Software : PyCharm
# 单引号和双引号里的内容只能一行 但三引号里的内容却可以多行
str1='人生苦短，我选python'
str2="人生苦短，我选python"
str3="""人生苦短，
我选python"""
str4='''人生苦短，
我选python'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))