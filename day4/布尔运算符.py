# -*- codeing = utf-8 -*-
# @Time : 2022/6/28 下午 8:48
# @Author : fengzhanwei
# @File : 布尔运算符.py
# @Software : PyCharm

#布尔运算
print('-------------and 并且----------')
a,b=1,2
print(a==1 and b==2) #true and true-->true
print(a==1 and b<2) #true and false-->false
print(a!=1 and b==2) #false and true-->false
print(a!=1 and b!=2) #false and false-->false

print('-------------or 或者----------')
print(a==1 or b==2) #true or true-->true
print(a!=1 or b==2) #false or true-->true
print(a==1 or b!=2) #true or false-->true
print(a!=1 or b!=2) #false or false-->false

print('-------------not 对bool类型的操作数取反----------')
f1=True
f2=False
print(not f1)
print(not f2)

print('-------------in与 not in----------')
s='hello world'
print('w' in s)#true
print('k' in s)#false
print('w' not in s) #false
print('k' not in s)#true


