# -*- codeing = utf-8 -*-
# @Time : 2022/7/8 下午 11:22
# @Author : fengzhanwei
# @File : for_in循环.py
# @Software : PyCharm
for item in 'Python': #第一次取出来的是P,将P赋值给item，将item的值输出
    print(item)

#range()产生一个整数序列，--》也是一个可迭代对象
for i in range(10):
    print(i)

#如果在循环体中不需要使用到自定义变量，可将自定义变量写为"_"
for _ in range(5):
    print("人生几何，我用python")

print("使用for循环，计算1到100之间的偶数和")
sum=0
for item in range(101):
    if item%2==0:
        sum+=item
print("1到100之间的偶数和为:",sum)

'''输出100到999之间的水仙花数
   举例：
   153=3*3*3+5*5*5+1*1*1
'''
for item in range(100,1000,1):
    ge=item%10 #个位
    shi=item//10%10 #十位
    bai=item//100 #百位、
    # print(bai,shi,ge)
    #判断
    if ge**3+shi**3+bai**3==item:
        print(item)