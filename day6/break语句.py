# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 下午 11:39
# @Author : fengzhanwei
# @File : break语句.py
# @Software : PyCharm
'''
从键盘录入密码，最多录入三次，如果正确就结束循环
'''
# for item in range(3):
#     pwd=input("请输入密码")
#     if pwd=='8888':
#         print("密码正确")
#         break
#     else:
#         print('密码错误')
# 二重循环中的break和continue,只控制本层循环
for i in range(5): #代表外层循环执行5次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5): #代表外层循环执行5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()