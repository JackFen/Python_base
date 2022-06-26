# -*- codeing = utf-8 -*-
# @Time : 2022/5/31 下午 3:25
# @Author : fengzhanwei
# @File : 整型.py
# @Software : PyCharm
# 可以输出数字
print(520)
print(98.5)
# 可以输出字符串
print('helloworld')
print("helloworld")

# 含义运算符的表达式
print(3+1)

# 将数据输出到文件中 注意点，1.所指定的盘符存在2、使用file=fp
fp=open('E:/text.txt','a+')
print('helloworld',file=fp)
fp.close()
# 不进行换行输出(输出内容在一行当中)
print('hello','world','python')