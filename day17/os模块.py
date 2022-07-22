# -*- codeing = utf-8 -*-
# @Time : 2022-07-22 上午 10:36
# @Author : fengzhanwei
# @File : os模块.py
# @Software : PyCharm

# os模块与操作系统相关的一个模块
import os
# os.system('notepad.exe') #打开记事本
# os.system('calc.exe') #打开计算器
# 直接调用可执行文件
# os.startfile(r'D:\Software\Wechat\WeChat.exe')

print(os.getcwd()) #返回当前的工作目录
lst=os.listdir('../day17')
print(lst)
# os.mkdir('newdir2') #创建目录
# os.makedirs('A/B/C') #创建多级目录
# os.rmdir('newdir2') #移除目录
# os.removedirs('A/B/C') #移除多级目录
os.chdir(r'D:\代码仓库\PycharmProjects\pythonLearn\LearnPython\base\day17') #将path设置为当前工作目录
print(os.getcwd())