# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 下午 3:38
# @Author : fengzhanwei
# @File : 集合的创建.py
# @Software : PyCharm

# 集合的创建
'''第一种创建方式：使用{}'''
s = {2, 3, 4, 5, 5, 6, 7, 7} #集合中的元素不允许重复
print(s)

'''第二种创建方式：使用set()'''

s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,4,5,5,6,7])
print(s2,type(s2))

s3=set((1,2,3,4,4,5,65)) #集合中的元素是无序的
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))

s5=set({12,3,4,56,7,8})
print(s5,type(s5))

# 定义一个空集合
s6=set()
print(s6,type(s6))