# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 下午 9:58
# @Author : fengzhanwei
# @File : 字典视图.py
# @Software : PyCharm
scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys)) #将所有的key组成的视图转换成列表

#获取所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values)) #将所有的values组成的视图转换成列表

#获取所有的key-value对
items=scores.items()
print(items) #元组()
print(list(items)) #转换之后的列表元素是由元组组成的
