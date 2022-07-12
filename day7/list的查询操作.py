# -*- codeing = utf-8 -*-
# @Time : 2022/7/10 下午 5:19
# @Author : fengzhanwei
# @File : list的查询操作.py
# @Software : PyCharm
lst=['hello','world',98,'hello']
print(lst.index('hello')) #如果列表中有相同的元素，只返回列表中相同元素的第一个元素的索引
# print(lst.index('python')) #ValueError: 'python' is not in list
print(lst.index('hello',1,4)) #左闭右开区间

lst2=['hello','world',98,'hello','world',234]
# 获取索引为2的元素 正向索引
print(lst2[2])
#获取索引为-3的元素 逆向索引
print(lst2[-3])

# 切片操作
lst=[10,20,30,40,50,60,70,80]
# start=1,stop=1,step=1
# print(lst[1:6:1]) #左闭右开，生成一个新的列表，步长默认为1

print('原列表：',id(lst))
lst2=lst[1:6:1]
print('切的片段：',id(lst2))
print(lst[1:6]) #步长默认为1
print(lst[1:6:])

# start=1,stop=1,step=2
print(lst[1:6:2])

#stop=6,start=2,start采用默认
print(lst[:6:2])

#start=1,step=2,stop采用默认
print(lst[1::2])

print('-------------step步长为负数的情况-----------')
print('原列表：',lst)
print(lst[::-1])
# start=7,stop省略,step=-1
print(lst[7::-1])
# start=6,stop=0,step=-2
print(lst[6:0:-2])