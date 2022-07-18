# -*- codeing = utf-8 -*-
# @Time : 2022-07-17 上午 11:07
# @Author : fengzhanwei
# @File : traceback使用.py
# @Software : PyCharm

import traceback
try:
    print('---------------')
    print(1/0)
except:
    traceback.print_exc()
