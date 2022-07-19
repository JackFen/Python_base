# -*- codeing = utf-8 -*-
# @Time : 2022-07-19 上午 9:15
# @Author : fengzhanwei
# @File : Object类的使用.py
# @Software : PyCharm

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name,self.age)
stu=Student('张三',20)
print(dir(stu)) #可以查看指定对象的所有属性
print(stu) #默认会调用__str__()方法
print(type(stu))