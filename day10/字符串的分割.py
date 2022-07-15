# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 3:05
# @Author : fengzhanwei
# @File : 字符串的分割.py
# @Software : PyCharm

s='hello world Python'
lst=s.split()
print(lst)
s1='hello|world|Python'
print(s1.split('|'))
print(s1.split('|',1))

'''rsplit()从右侧开始劈分'''
print(s.rsplit())
print(s1.rsplit('|'))
print(s1.rsplit('|',1))