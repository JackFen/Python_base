# -*- codeing = utf-8 -*-
# @Time : 2022/7/9 下午 8:24
# @Author : fengzhanwei
# @File : continue语句.py
# @Software : PyCharm

'''要求输出1到50之间所有5的倍数，5,10,15,20,25,30......
   5的倍数的共同点：和5的余数为0的数都是5的倍数
'''
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)