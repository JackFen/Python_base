# -*- codeing = utf-8 -*-
# @Time : 2022-07-16 上午 11:17
# @Author : fengzhanwei
# @File : 函数的定义与调用.py
# @Software : PyCharm
def calc(a,b): #a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c=a+b
    return c
result=calc(10,20) #10,20,称为实际参数的值，简称实参，实参的位置是函数的调用处 位置传参
print(result)

res=calc(b=20,a=10) #左侧的变量名称称为关键字参数
print(res)

def fun(arg1,arg2):
    print(arg1)
    print(arg2)
    arg1=100
    arg2.append(10)
    print(arg1)
    print(arg2)

n1=11
n2=[22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2) #位置传参，arg1,arg2是函数定义处的形参，n1,n2是函数调用处的实参，总结：实参名称和形参名称可以不一致
print('n1',n1)
print('n2',n2)

'''在函数的调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值，arg1修改为100，不会影响n1的值
如果是可变对象，在函数的修改会影响到实参的值 arg2修改为.append(10),会影响到n2的值
'''

'''函数的返回值'''
# 分类奇数与偶数
def find(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

# 函数的调用
lst=[10,29,34,23,44,53,55]
print(find(lst))

'''函数的返回值
   （1）如果函数没有返回值【函数执行完毕后，不需要给调用处提供数据】return可以省略不写
   （2）函数的返回值，如果是一个，直接返回类型
   （3）函数的返回值，如果是多个，返回结果为元组
'''

def fun1():
    print('hello')

fun1()
def fun2():
    return 'hello'

res=fun2()
print(res)

def fun3():
    return 'hello','world'

print(fun3())
'''函数在定义时，是否需要返回值，视情况而定'''