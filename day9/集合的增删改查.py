# -*- codeing = utf-8 -*-
# @Time : 2022-07-14 下午 8:49
# @Author : fengzhanwei
# @File : 集合的增删改查.py
# @Software : PyCharm
s={10,20,30,405,60}
'''集合元素的判断操作'''
print(10 in s) #True
print(100 in s) #False
print(10 not in s) #False
print(100 not in s) #True
'''集合元素的新增操作'''
s.add(80) #一次添加一个元素
print(s)
s.update({200,400,300}) #一次至少添加一个元素
print(s)
s.update([100,200,300])
s.update((78,59,30))
print(s)
'''集合元素的删除操作'''
s.remove(100)
print(s)
# s.remove(500) #KeyError: 500 元素不存在会抛异常
s.discard(500) #元素不存在不会抛异常
s.discard(300)
print(s)
s.pop() #删除队首元素
print(s)
s.clear()
print(s)