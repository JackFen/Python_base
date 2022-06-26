# -*- codeing = utf-8 -*-
# @Time : 2022/6/26 下午 11:30
# @Author : fengzhanwei
# @File : 运算符.py
# @Software : PyCharm

print(1+1) #加法运算
print(1-1) #减法运算
print(2*4) #乘法运算
print(11/2) # 5.5除法运算
print(11//2) # 5 整除运算
print(11%2) #1 取余运算
print(2**3) #表示的是2的3次方
print(9//-4)#-3一正一负向下取整
print((-9//4))#-3
print(9%-4)#-3  公式：余数=被除数-除数*商 9-（-4）*3=-3
print(-9%4)#3  -9-4*(-3)=3

#赋值运算符，运算顺序从右到左

i=3+4
print(i)
a=b=c=20 #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))
print('-------支持参数赋值---------')
a=20
a+=30 #相当于a=a+30
print(a)
a-=10 #相当于a=a-10
print(a)
a*=2 #相当于a=a*2
print(a)
a//=3
print(a)
a%=2
print(a)
print('-------支持解包赋值---------')
a,b,c=20,30,40
print(a,b,c)
print('-------交换两个变量的值---------')
a,b=10,20
print('交换之前',a,b)
a,b=b,a
print('交换之后',a,b)