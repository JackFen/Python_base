# -*- codeing = utf-8 -*-
# @Time : 2022/4/20 下午 2:56
# @Author : fengzhanwei
# @File : 整型.py
# @Software : PyCharm

#字符串有 单引号 双引号 三引号
word = '字符串'
setence="这是一个句子"
paragraph="""
            这是一个段落
            可以由多行组成
"""

'''
#my_str="I'am a student"
my_str='I\'am a student'
print(my_str)
'''

'''
#my_str="Jason said \"I like you\""
my_str='Jason said "I like you"'
print(my_str)
'''

str="chengdu"

'''
print(str)
print(str[0])
print(str[0:5])  #[起始位置:结束位置:步进值]
print(str[1:7:2])
'''
'''
print(str[:5])
print(str[5:])

print(str+",你好") #字符串连接使用+
print(str*3)      #重复打印使用*
'''

print("hello\nchengdu") #使用反斜杠实现转义字符的功能

print(r"hello\nchengdu") #在字符串前面加个r 表示直接显示原始字符串，不进行转义

