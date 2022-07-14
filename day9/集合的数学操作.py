# -*- codeing = utf-8 -*-
# @Time : 2022-07-14 下午 9:12
# @Author : fengzhanwei
# @File : 集合的数学操作.py
# @Software : PyCharm

#（1）交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2) #intersection()和 & 是等价的

#（2）并集操作
print(s1.union(s2))
print(s1 | s2) #union()和 | 是等价的

#（3）差集操作
print(s1.difference(s2))
print(s1-s2) #difference()和 - 是等价的

#(4)对称差集操作
print(s1.symmetric_difference(s2))
print(s1 ^ s2) #symmetric_difference()和 ^是等价的