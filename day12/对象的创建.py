# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 下午 12:21
# @Author : fengzhanwei
# @File : 对象的创建.py
# @Software : PyCharm
class Student:  # Student为类的名称（类名）（规范）每个单词的首字母大写，其余小写
    native_pace = '河北'  # 直接写在类里面的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):  # 要写上self
        print('学生在吃饭...')

    # 静态方法
    @staticmethod
    def method():  # 不允许写self
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):  # 要写上cls，即class
        print('我是类方法，因为我使用了classmethod进行修饰')

# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')

# 创建Student类的对象
stu1=Student('张三','20')
# print(id(stu1))  #其id 2335134866784（十进制）与<__main__.Student object at 0x0000021FB0E25D60> 里的八进制数相等
# print(type(stu1))
# print(stu1)
# print('-------------')
# print(id(Student)) #Student是类的名称
# print(type(Student))
# print(Student)

stu1.eat()   #对象名.方法名
print(stu1.name)
print(stu1.age)

print('------------------')
Student.eat(stu1) #46行与41行代码相同，都是调用Student中的eat方法
                  #类名.方法名（类的对象）-->实际上就是方法定义处的self