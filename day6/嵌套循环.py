# -*- codeing = utf-8 -*-
# @Time : 2022/7/9 下午 8:46
# @Author : fengzhanwei
# @File : 嵌套循环.py
# @Software : PyCharm

# 输出一个三行四列的矩形
for i in range(1,4): #行表，执行三次，一次是一行
    for j in range(1,5):
        print('*',end='\t') #不换行输出
    print() #换行
print('直角三角形')
for i in range(1,10):
    for j in range(1,i+1):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

print('九九乘法表')

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j, end='\t')  # 不换行输出
    print()  # 换行