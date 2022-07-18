# -*- codeing = utf-8 -*-
# @Time : 2022-07-18 上午 10:08
# @Author : fengzhanwei
# @File : 方法重写.py
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
    def info(self):
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,TeachOfYear):
        super().__init__(name,age)
        self.TeachOfYear=TeachOfYear
    def info(self):
        super().info()
        print('教龄为'+str(self.TeachOfYear))

stu=Student('张三',20,'1001')
tea=Teacher('李四',34,10)

stu.info()
print('-------------')
tea.info()

