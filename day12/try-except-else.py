# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 上午 10:51
# @Author : fengzhanwei
# @File : try-except-else.py
# @Software : PyCharm
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)