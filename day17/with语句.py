# -*- codeing = utf-8 -*-
# @Time : 2022-07-22 上午 10:13
# @Author : fengzhanwei
# @File : with语句.py
# @Software : PyCharm

# #文件操作离开with语句自动关闭文件
# print(type(open('a.txt','r',encoding='utf-8')))
# with open('a.txt','r',encoding='utf-8') as file:
#     print(file.read())

'''MyContentMgr实现了特殊方法__enter__，__exit__ 则称该类对象遵守上下文管理器协议
该类对象的实例对象称为上下文管理器
MyContentMgr()
'''
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')
        return self
    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as file: #相当于file=MyContentMgr(),无论with语句中是否产生异常，都会调用exit方法
    file.show()

with(open('a.txt','r',encoding='utf-8')) as src_file:
    with(open('b.txt','w',encoding='utf-8')) as target_file:
        target_file.write(src_file.read())
