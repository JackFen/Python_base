# -*- codeing = utf-8 -*-
# @Time : 2022/6/30 下午 8:38
# @Author : fengzhanwei
# @File : 嵌套if的使用.py
# @Software : PyCharm
"""
     会员 >=200 8折
            >=100 9折
           不打折
     非会员 >=200 9.5折
           不打折
"""
anwser=input('您是会员吗？y/n')
money=float(input('请输入你的购物金额：'))
#外层判断是否为会员
if anwser=='y':#会员
    if money>=200:
        print('打8折，付款金额为：',money*0.8)
    elif money>=100:
        print('打9折，付款金额为：', money * 0.9)
    else:
        print('不打折，付款金额为',money)
else:
    if money>=200:
        print('打95折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为', money)
