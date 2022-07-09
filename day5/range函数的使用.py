# -*- codeing = utf-8 -*-
# @Time : 2022/6/30 下午 9:07
# @Author : fengzhanwei
# @File : range函数的使用.py
# @Software : PyCharm
# range()的三种创建方式
"""
第一种创建方式，只有一个参数（小括号中只给了一个数stop）
"""
r=range(10)
print(r) #range(0, 10)
print(list(r)) #用于查看range对象中的整数序列  -->list是列表的意思 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认从0开始，默认步进值为1
"""
第二种创建方式，有两个参数（小括号中给了start和stop）
"""
r=range(1,10) #指定了起始，从1开始，到9结束不包含10
print(list(r))#[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
第三种创建方式，有三个参数（小括号中给了start,stop和step）
"""
r=range(1,10,2)
print(list(r))#[1, 3, 5, 7, 9]

"""判断指定的整数在序列中是否存在in ,not in"""
print(10 in r)#False
print(9 in r)#True
print(10 not in r)#True
print(9 not in r)#False
