# -*- codeing = utf-8 -*-
# @Time : 2022-07-20 上午 11:00
# @Author : fengzhanwei
# @File : 模块的导入.py
# @Software : PyCharm

import math #关于数学的模块
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('--------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3))) #8.0 <class 'float'>
print(math.ceil(9.001)) #10 找和输入数据相近的最大整数
print(math.floor(9.999)) #9 找和输入数据相近的最小整数

print('--------------')
#只想使用math中的pi
from math import pi
print(pi)

# 若不导入math中的pow，则两个pow所属的模块不一样
print(pow(2,3))
print(math.pow(2,3))

