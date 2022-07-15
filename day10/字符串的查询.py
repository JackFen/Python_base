# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 2:41
# @Author : fengzhanwei
# @File : 字符串的查询.py
# @Software : PyCharm
s='hello,hello'
print(s.index('lo')) #3
print(s.find('lo')) #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9

# print(s.index('k')) #ValueError: substring not found
print(s.find('k')) #-1
# print(s.rindex('k')) #ValueError: substring not found
print(s.rfind('k')) #-1