# -*- codeing = utf-8 -*-
# @Time : 2022/4/20 下午 2:21
# @Author : fengzhanwei
# @File : demo4.py
# @Software : PyCharm
'''
for i in range(5):
    print(i)
'''

'''
for i in range(0,10,3):   #从0开始，到10结束，步进值为3（+3）
    print(i)
'''

'''
for i in range(-10,-100,-10):
    print(i)
'''

'''
name="chengdu" #可以遍历字符串

for x in name:
    print(x,end="\t")
'''

'''
a=["aa","bb","cc","dd"] #也可以遍历list列表

for i in range(len(a)):
    print(i,a[i])
'''

'''
i=0
while i<5:
    print("当前是第%d次循环"%(i+1))
    print("i=%d"%i)
    i=i+1
'''

'''
 #1-100求和
i=1
sum=0
while i<101:
    sum=sum+i
    i+=1
print("和为%d"%sum)
'''

'''
count=0   #while可以和else一起使用
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于或等于5")
'''

'''
i=0
while i<10:
    i+=1
    print("-"*30)
    if i==5:
        break   #结束整个while循环
    print(i)
'''

'''
i=0
while i<10:
    i+=1
    print("-"*30)
    if i==5:
        continue   #结束本次循环
    print(i)
'''
#作业：使用for循环和while循环，打印九九乘法表
j=1
for i in range(1,10,1):
    while j<=i:
        print("%d*%d=%d"%(i,j,(i*j)),end="\t")
        j+=1
    j=1
    print()