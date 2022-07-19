# -*- codeing = utf-8 -*-
# @Time : 2022-07-19 上午 9:22
# @Author : fengzhanwei
# @File : 多态.py
# @Software : PyCharm
class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')
class Person:
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('----------------')
fun(Person())