# -*- codeing = utf-8 -*-
# @Time : 2022/6/29 下午 8:52
# @Author : fengzhanwei
# @File : 分支结构.py
# @Software : PyCharm
money=1000 #余额
s=int(input('请输入取款金额')) #取款金额
#判读余额是否充足
if money>=s:
    money-=s
    print('取款成功，余额为：',money)
else:
    print('取款失败')