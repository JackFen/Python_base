# -*- codeing = utf-8 -*-
# @Time : 2022/7/12 下午 8:11
# @Author : fengzhanwei
# @File : List增加操作.py
# @Software : PyCharm
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100) #在尾部添加一个元素
print('添加元素之后',lst,id(lst))
lst2=['hello','world']
# lst.append(lst2) #将lst2作为一个元素添加到列表的末尾
lst.extend(lst2) #向列表的末尾一次性添加多个元素
print(lst)

#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
#在任意的位置上添加N多个元素,切片，替换
lst[1:]=lst3
print(lst)