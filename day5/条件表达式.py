# -*- codeing = utf-8 -*-
# @Time : 2022/6/30 下午 8:48
# @Author : fengzhanwei
# @File : 条件表达式.py
# @Software : PyCharm
"""
从键盘录入两个整数，比较两个整数的大小
"""
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
# 比较大小
print('使用条件表达式进行比较')
print(str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))