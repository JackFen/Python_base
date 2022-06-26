# -*- codeing = utf-8 -*-
# @Time : 2022/6/26 上午 1:20
# @Author : fengzhanwei
# @File : 浮点数.py
# @Software : PyCharm
a = 3.141592
print(a, type(a))
n1=2.2
n2=1.1
n3=2.1
print(n1+n2)
print(n1+n3)

from decimal import Decimal
print((Decimal('1.1')+Decimal('2.2')))
