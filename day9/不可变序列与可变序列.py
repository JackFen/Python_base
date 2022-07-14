# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 下午 3:04
# @Author : fengzhanwei
# @File : 不可变序列与可变序列.py
# @Software : PyCharm

'''可变序列：列表，字典'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列：字符串，元组'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))
print(s)

t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100'''
# t[1]=100 #TypeError: 'tuple' object does not support item assignment 元组是不允许修改元素的
'''由于[20,30]列表。而列表是可变序列，所有可以向列表中添加元素，而列表的内存地址不变'''
t[1].append(100) #向列表添加元素
print(t)