# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 2:56
# @Author : fengzhanwei
# @File : 字符串内容对齐操作.py
# @Software : PyCharm

s='hello,Python'
'''居中对齐'''
print(s.center(20,'*'))
'''左对齐'''
print(s.ljust(20,'*'))
print(s.ljust(10,'*'))#填充不够返回原字符串
print(s.ljust(20)) #第二个参数不写默认为空格
'''右对齐'''
print(s.rjust(20,'*'))
print(s.rjust(10,'*'))#填充不够返回原字符串
print(s.rjust(20)) #第二个参数不写默认为空格

'''右对齐，使用0进行填充'''
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))