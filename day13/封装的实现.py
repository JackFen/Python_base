# -*- codeing = utf-8 -*-
# @Time : 2022-07-18 上午 9:53
# @Author : fengzhanwei
# @File : 封装的实现.py
# @Software : PyCharm

class Car:
    def __init__(self,band):
        self.band=band
    def start(self):
        print('汽车已启动...')

car=Car('兰博基尼')
car.start()
print(car.band)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #年龄不希望在类的外部被使用，所以加了两个
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
# 在类的外部使用name和age
print(stu.name)
# print(stu.__age)
# print(dir(stu))
print(stu._Student__age) #在类的外部可以通过 _Student__age 进行访问
