# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 3:29
# @Author : fengzhanwei
# @File : 字符串的替换与合并.py
# @Software : PyCharm

s='hello,Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))
lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))
print('*'.join('python'))