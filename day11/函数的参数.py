# -*- codeing = utf-8 -*-
# @Time : 2022-07-16 下午 12:40
# @Author : fengzhanwei
# @File : 函数的参数.py
# @Software : PyCharm

def fun(a,b=10): #b称为默认值参数
    print(a,b)

#函数的调用
fun(100)
fun(20,30)

'''参数个数不确定'''
def fun1(*args): #函数定义时的 可变的位置参数
    print(args)
    # print(args[0])

fun1(10)
fun1(10,30)
fun1(30,40,50)

def fun2(**args):
    print(args)

fun2(a=10)
fun2(a=1,b=2)
fun2(a=1,b=2,c=3)

'''def fun3(*args,*a):
    pass
    以上代码会报错，个数可变的位置参数只能有一个

def fun4(**args,**a):
 pass
 以上代码会报错，个数可变的关键字参数只能有一个
'''

def fun3(*args1,**args2):
    pass

'''
def fun4(**args1,*args2):
    pass
    在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，个数可变的位置形参，放在个数可变的关键字形参之前
'''

def fun4(a,b,c): #函数调用时的参数传递，称为位置传参
    print('a=',a)
    print('b=',b)
    print('c=',c)

#函数的调用
fun4(10,20,30) #函数调用时的参数传递，称为位置传参
lst=[11,22,33]
fun4(*lst) #在函数调用时，将列表中的每个元素都转换为位置实参传入

fun4(a=100,b=200,c=300) #函数的调用，所以是关键字实参
dic={'a':111,'b':222,'c':333}
fun4(**dic)

def fun5(a,b=10):
    print('a=',a)
    print('b=',b)

def fun6(*args):
    print(args)

def fun7(**args):
    print(args)

fun6(10,20,30,40)
fun7(a=11,b=2,c=4)

def fun8(a,b,*,c,d): #从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a=',a)
    print('b=',b)
    print('c=', c)
    print('d=', d)

# 调用fun8函数
# fun8(10,20,30,40) #位置实参传递
fun8(a=10,b=20,c=30,d=40) #关键字实参传递
fun8(10,20,c=30,d=40) #前两个参数，采用的是位置实参传递，而c,d采用的是关键字实参传递
''' 需求  c,d只能采用关键字实参传递'''

'''函数定义时的形参顺序问题'''
def fun9(a,b,*,c,d,**args):
    pass

def fun10(*args,**args2):
    pass

def fun11(a,b=10,*args1,**args2):
    pass
