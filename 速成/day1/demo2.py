# -*- codeing = utf-8 -*-
# @Time : 2022/4/19 下午 9:34
# @Author : fengzhanwei
# @File : 整型.py
# @Software : PyCharm

'''
print("标准化输出字符串")
a=10
print("这是变量",a)
'''
'''

# 格式化输出
age=18
print("我的年纪是：%d 岁"%age)
print("我的名字是%s,我的国籍是%s"%("jack","中国"))

print("aaa","bbb","ccc")
print("www","baidu","com",sep=".") #sep= 表示用什么来分割字符串
print("hello",end="")              #end= 表示用什么来结尾
print("world",end="\t")
print("python",end="\n")
print("end")
'''

'''
password=input("请输入密码:\n")
print("您刚输入的密码是：",password)
'''

'''
#a=10
#a="abc"
a=input("输入：")
print(type(a))

print("输入了一个数字：%s" %a)
'''

'''
a=int("123")#强制类型转换
b=a+100
print(b)
print(type(b))
'''
c=int(input("输入c"))
print("输入了一个数字：%d" %c)
