# -*- codeing = utf-8 -*-
# @Time : 2022/7/9 下午 8:33
# @Author : fengzhanwei
# @File : else语句.py
# @Software : PyCharm
# for item in range(3):
#     pwd=input('请输入密码：')
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
# else:
#     print('对不起，三次密码均输入错误')

# 与while结合使用
a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a=a+1 #改变变量
else:
    print('对不起，三次密码均输入错误')