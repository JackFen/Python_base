# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 上午 11:30
# @Author : fengzhanwei
# @File : 类的创建.py
# @Software : PyCharm

class Student: #Student为类的名称（类名）（规范）每个单词的首字母大写，其余小写
    native_pace='河北'  #直接写在类里面的变量，称为类属性
    def __init__(self,name,age):
        self.name=name #self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age=age
    #实例方法
    def eat(self): #要写上self
        print('学生在吃饭...')
    # 静态方法
    @staticmethod
    def method(): #不允许写self
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls): #要写上cls，即class
        print('我是类方法，因为我使用了classmethod进行修饰')

# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
        print('喝水')

# 类属性的使用方式
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',25)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('--------类方法的使用方式---------')
Student.cm()
print('--------静态方法的使用方式---------')
Student.method()