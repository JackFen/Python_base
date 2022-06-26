# -*- codeing = utf-8 -*-
# @Time : 2022/6/26 上午 1:41
# @Author : fengzhanwei
# @File : 类型转化.py
# @Software : PyCharm
name='张三'
age=20
print(type(name), type(age)) #说明name与age的数据类型不相同
# 当将str类型与int类型进行连接的时候，报错，解决办法：类型转换
print('我叫'+name+'今年，'+str(age)+'岁') #将int累心通过str()函数转换成了str类型
print("-------str()将其它来类型转换成str类型---------")
a=10
b=189.8
c=False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)),type(str(c)))
print("-------int()将其它来类型转换成int类型---------")
s1='128'
f1=98.7
s2="76.77"
ff=True
s3="hello"
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1), type(int(s1))) #将str转成int类型，字符串为数字串
print(int(f1),type(int(f1))) #float转化为int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) #将str转换为int类型，报错，因为字符串为小数串
print(int(ff), type(int(ff)))
#print(int(s3), type(int(s3))) #将str转为int类型的时候，字符串必须为数字串（整数），非数字串是不允许转换的
print("-------float()函数，将其它数据类型转换成float类型---------")
s1='128.98'
s2="76.77"
ff=True
s3="hello"
i=98
print(type(s1), type(s2), type(ff), type(s3), type(i))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(ff), type(float(ff)))
# print(float(s3), type(float(s3))) #字符串中的数据如果是非字符串，则不允许转换