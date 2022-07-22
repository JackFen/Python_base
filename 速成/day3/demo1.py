# -*- codeing = utf-8 -*-
# @Time : 2022/4/23 上午 8:30
# @Author : fengzhanwei
# @File : 整型.py
# @Software : PyCharm
'''
def printinfo(): #函数的定义
    print("-"*30)
    print("      人生苦短，我用python")
    print("-"*30)
printinfo()
'''
'''
#带参的函数
def add2Num(a,b):
    c=a+b
    print(c)
add2Num(11,22)
'''
'''
#带返回值的函数

def add2Num(a,b):
    return a+b #通过return来返回运算结果

print(add2Num(11,33))
'''
'''
#返回多个值的函数

def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu    #多个返回值用逗号分割

sh,yu=divid(5,2)   #需要使用多个值来保存返回内容

print("商：%d,余数：%d"%(sh,yu))
'''
'''
#课堂练习

#打印一条线
def printline():
    print("-"*30)
#根据用户输入的数字来打印相应条数的线
def printline2(n):
    for i in range(0,n,1):
        printline()
def sum3Num(a,b,c):
    return a+b+c
def avg3Num(a,b,c):
    return sum3Num(a,b,c)/3.0
'''
'''
#全局变量和局部变量

def test1():
    a=300 #局部变量
    print("test1修改前：a=%d"%a)
    a=100
    print("test1修改后: a=%d"%a)
def test2():
    a=500 #不同函数可以定义相同的名字，彼此无关
    print("test2：a=%d" %a)

test1()
test2()
'''
'''
a=100  #全局变量
def test1():
    print(a)
def test2():
    print(a)  #调用全局变量a

test1()
test2()
'''
'''
#全局变量和局部变量相同名字
a=100  #全局变量
def test1():
    a=300 #局部变量优先使用
    print("test1修改前：a=%d"%a)
    a=100
    print("test1修改后: a=%d"%a)
def test2():
    print("test2：a=%d" %a) #没有局部变量，默认使用全局变量

test1()
test2()
'''
#在函数中修改全局变量
a=100  #全局变量
def test1():
    global a  #申明全局变量在函数中的标识符
    print("test1修改前：a=%d"%a)
    a=200
    print("test1修改后: a=%d"%a)
def test2():
    print("test2：a=%d" %a) #没有局部变量，默认使用全局变量

test1()
test2()