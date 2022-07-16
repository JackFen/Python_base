# -*- codeing = utf-8 -*-
# @Time : 2022-07-16 下午 4:51
# @Author : fengzhanwei
# @File : 递归函数.py
# @Software : PyCharm

def fac(n):
    if n<=1:
        return 1
    else:
        return fac(n-1)*n

print(fac(6))

def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# 斐波那切数列
print(fib(6))

print('---------------------')
# 输出这个数列前n位上的数字
for i in range(1,7):
    print(fib(i))