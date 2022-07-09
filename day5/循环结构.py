# -*- codeing = utf-8 -*-
# @Time : 2022/6/30 下午 9:22
# @Author : fengzhanwei
# @File : 循环结构.py
# @Software : PyCharm
a=1
# while循环
#判断条件表达式
while a<10:
    print(a)
    a+=1
"""
4步循环法
 1.初始化变量
 2.条件判断
 3.条件执行体（循环体）
 4.改变变量
 总结：初始化的变量与条件判断的变量为同一个
"""
"""
计算1到100之间的偶数和
"""
b=1
sum=0
while b<101:
    if not bool(b%2):
        sum+=b
    b+=1
print(sum)