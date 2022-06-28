# -*- codeing = utf-8 -*-
# @Time : 2022/6/28 下午 9:36
# @Author : fengzhanwei
# @File : 对象的bool值.py
# @Software : PyCharm
#测试对象的bool值
print('----------以下对象的bool值为false--------')
print(bool(False)) #false
print(bool(0)) #false
print(bool(0.0)) #false
print(bool(None)) #false
print(bool('')) #false
print(bool("")) #false
print(bool([])) #空列表
print(bool(list())) #空列表
print(bool(())) #空元组
print(bool(tuple())) #空元组
print(bool({})) #空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
print('----------其它对象的bool值均为true--------')
print(bool(18))
print(bool(True))