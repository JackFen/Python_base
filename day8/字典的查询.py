# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 上午 10:51
# @Author : fengzhanwei
# @File : 字典的查询.py
# @Software : PyCharm
'''获取字典中的元素'''
scores={'张三':100,'李四':98,'王五':45}
'''第一种方式,使用[]'''
print(scores['张三'])
# print(scores['陈六']) #查找值不存在，KeyError: '陈六' 会报错

'''第二种方式，使用get()方法'''
print(scores.get('张三'))
print(scores.get('陈六')) #查找值不存在，None 不会报错
print(scores.get('麻七',99)) #99是在查找‘麻七’所对应的value不存在所对应的value不存在时，提供的一个默认值
