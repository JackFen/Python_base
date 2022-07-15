# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 4:03
# @Author : fengzhanwei
# @File : 字符串的比较.py
# @Software : PyCharm

print(('apple'>'app')) #True
print('apple'>'banana') #False
print(ord('a'),ord('b')) #97 98
print(ord('冯'))
print(chr(97),chr(98)) #a b
print(chr(20911))

'''==与is的区别
 ==比较的是value
 is 比较的是id是否相等'''
a=b='Python'
c='Python'
print(a==b) #True
print(b==c) #True
print(a is b) #True
print(a is c) #True
