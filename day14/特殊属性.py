# -*- codeing = utf-8 -*-
# @Time : 2022-07-19 上午 9:31
# @Author : fengzhanwei
# @File : 特殊属性.py
# @Software : PyCharm

# print(dir(object))
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
# 创建C类对象
x=C('jack',20) #x是C类型的实例对象
print(x.__dict__) #实例对象的属性字典 {'name': 'jack', 'age': 20}
print(C.__dict__) #{'__module__': '__main__', '__init__': <function C.__init__ at 0x0000014894C6E1F0>, '__doc__': None}
print(x.__class__) #<class '__main__.C'> 输出了对象所属的类
print(C.__bases__) #(<class '__main__.A'>, <class '__main__.B'>) C的父类类型的元组
print(C.__base__) #输出C优先继承的父类类型 <class '__main__.A'>
print(C.__mro__) #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)类的层次结构
print(A.__subclasses__()) #[<class '__main__.C'>, <class '__main__.D'>] 子类的列表