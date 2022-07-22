# -*- codeing = utf-8 -*-
# @Time : 2022/4/23 上午 9:02
# @Author : fengzhanwei
# @File : 浮点数.py
# @Software : PyCharm
'''
f=open("text.txt","w")  #打开文件，w模式（写模式），文件不存在就新建
f.write("hello,I am here!")  #将字符串写入到文件中
f.close()  #关闭文件
'''

'''  
#read方法，读取指定的字符，开始时定位在文件的头部，每执行一次向后移动指定字符数
f=open("text.txt","r")

content=f.read(5)

print(content)

content=f.read(5)
print(content)
f.close()
'''
'''
f=open("text.txt","r")
content=f.readlines()  #一次性读取全部文件为列表，每一行一个字符串元素
#print(content)

i=1
for temp in content:
    print("%d:%s"%(i,temp))
    i+=1
f.close()
'''
'''
f=open("text.txt","r")
content=f.readline()
print("1:%s"%content)
content=f.readline()
print("2:%s"%content)
f.close()
'''
import os
os.rename("text.txt","text1.txt")