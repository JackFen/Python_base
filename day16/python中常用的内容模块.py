# -*- codeing = utf-8 -*-
# @Time : 2022-07-21 上午 11:16
# @Author : fengzhanwei
# @File : python中常用的内容模块.py
# @Software : PyCharm

import sys
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

import math
print(math.pi)
