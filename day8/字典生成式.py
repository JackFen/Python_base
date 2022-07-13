# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 下午 10:36
# @Author : fengzhanwei
# @File : 字典生成式.py
# @Software : PyCharm

items=['Fruits','Books','Others']
prices=[96,78,85,100,200]

d={item:price for item,price in zip(items,prices)} #打包时以短的列表为基准
print(d)