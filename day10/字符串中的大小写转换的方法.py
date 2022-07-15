# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 2:47
# @Author : fengzhanwei
# @File : 字符串中的大小写转换的方法.py
# @Software : PyCharm

s='hello,python'
a=s.upper() #转成大写之后，会产生一个新的字符串对象
print(a,id(a)) #HELLO,PYTHON
print(s,id(s))
print(s.lower(),id(s.lower())) #即使转换之后和原先没区别，但也会产生一个新的字符串对象

s2='hello,Python'
print(s2.swapcase()) #大写变小写，小写变大写
print(s2.title()) #每个单词的首字母变成大写