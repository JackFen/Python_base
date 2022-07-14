# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 下午 3:32
# @Author : fengzhanwei
# @File : 元组的遍历.py
# @Software : PyCharm

'''元组的遍历'''
t=('python','world',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) #IndexError: tuple index out of range

'''遍历元组'''
for item in t:
    print(item)