# -*- codeing = utf-8 -*-
# @Time : 2022-07-18 上午 10:08
# @Author : fengzhanwei
# @File : 继承的实现.py
# @Software : PyCharm
class Person(object): #Person类继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,TeachOfYear):
        super().__init__(name,age)
        self.TeachOfYear=TeachOfYear

stu=Student('张三',20,'1001')
tea=Teacher('李四',34,10)

stu.info()
tea.info()

# 多继承

class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass