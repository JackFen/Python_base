# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 上午 10:44
# @Author : fengzhanwei
# @File : try-except.py
# @Software : PyCharm
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为',result)
except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')