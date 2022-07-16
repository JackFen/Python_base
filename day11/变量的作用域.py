# -*- codeing = utf-8 -*-
# @Time : 2022-07-16 下午 4:41
# @Author : fengzhanwei
# @File : 变量的作用域.py
# @Software : PyCharm

def fun(a,b):
    c=a+b #c就称为局部变量，因为c是在函数体内进行定义的变量，a,b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

# print(c) ，因为a,c超出了起作用的范围（超出了作用域）
# print(a)

name='JackFeng'
print(name)
def fun2():
    print(name)

# 调用函数
fun2()

def fun3():
    global age #函数内部的变量是局部变量，局部变量使用global声明，这个变量实际上就变成了全局变量
    age=20
    print(age)
fun3()
print(age)