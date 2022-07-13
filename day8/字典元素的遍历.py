# -*- codeing = utf-8 -*-
# @Time : 2022/7/13 下午 10:05
# @Author : fengzhanwei
# @File : 字典元素的遍历.py
# @Software : PyCharm
scores={'张三':100,'李四':98,'王五':45}
#字典元素的遍历
for item in scores:
    print(item,scores[item],scores.get(item))
