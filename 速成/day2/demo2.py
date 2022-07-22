# -*- codeing = utf-8 -*-
# @Time : 2022/4/20 下午 3:21
# @Author : fengzhanwei
# @File : 浮点数.py
# @Software : PyCharm

#namelist=[] #定义一个空的列表


namelist=["小张","小王","小李"]
testlist=[1,"测试"]  #列表中可以存储混合类型
'''
print(namelist)
print(namelist[0])
print(namelist[1])

print(type(testlist[0]))
print(type(testlist[1]))
'''

'''
for name in namelist:
    print(name)

#print(len(namelist)) #len()可以得到列表的长度

lenth=len(namelist)
i=0

while i<lenth:
    print(namelist[i])
    i+=1
'''
'''
#增：【append】

print("----增加前名单列表的数据-----")
for name in namelist:
    print(name)
nametemp=input("请输入添加学生的姓名：")
namelist.append(nametemp)#在末尾追加一个元素

print("----增加后名单列表的数据-----")
for name in namelist:
    print(name)
'''

'''
a=[1,2]
b=[3,4]
a.append(b) #将列表当做一个元素加入到列表中
print(a)

#增：【extend】
a.extend(b) #将b列表中的每一个元素逐一追加到a列表中
print(a)
'''

'''
#增：【insert】
a=[0,1,2]
a.insert(1,3) #第一个变量表示下标，第二个元素表示元素（对象）
print(a)     #指定下标位置插入元素
'''

'''
#删 【del】 【pop】【remove】

movieName=["加勒比海盗","骇客帝国","第一滴血","指环王","速度与激情"]
print("----删除前名单列表的数据-----")
for name in movieName:
    print(name)
#del movieName[2]#在指定位置删除一个元素
#movieName.pop()  #弹出末尾最后一个元素
#movieName.remove("指环王") #直接删除指定内容的第一个元素
print("----删除后名单列表的数据-----")
for name in movieName:
    print(name)
'''

'''
#改 :
print("----增加前名单列表的数据-----")
for name in namelist:
    print(name)
namelist[1]="小红" #修改指定下标的内容
print("----增加后名单列表的数据-----")
for name in namelist:
    print(name)
'''

'''
#查：【in,not in】
findName=input("请输入你要查找的学生姓名：")
if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")
'''
mylist=["a","b","c","a","b"]

'''
print(mylist.index("a",1,4)) #可以查找指定下标范围的元素，并返回找到对应数据的下标
print(mylist.index("a",1,3)) #范围区间左开右闭 【1,3）
                             #找不到会报错
'''

'''
print(mylist.count("c"))  #统计某个元素出现几次
'''
'''
#排序和反转
a=[1,4,2,3]
print(a)
a.reverse()  #将列表所有元素反转
print(a)

a.sort() #升序排序
print(a)
a.sort(reverse=True) #降序
print(a)
'''

'''
#schoolNames=[[],[],[]]  #有三个元素的空列表，每个元素都是一个空列表

schoolName=[["北京大学","清华大学"],["南开大学","天津大学","天津师范大学"],["山东大学","中国海洋大学"]]

print(schoolName[0])
print(schoolName[0][0])

import random
offices=[[],[],[]]
names=["A","B","C","D","E","F","G","H"]
for name in names:
    index=random.randint(0,2)#左闭右闭区间
    offices[index].append(name)
i=1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end='\t')
    print("\n")
    print("-"*20)
'''
#作业 根据上面的products列表写一个循环，不断询问用户想买什么，
# 用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表
products=[["iphone",6888],["MacPro",14800],["mi6",2499],["Coffee",31],["Book",60],["Nike",699]]
carts=[]
while True:
    i=0
    print("-"*6+"商品列表"+"-"*6)
    for product in products:
        print("%d  %-10s%-5d"%(i,product[0],product[1]))
        i+=1
    answer=input("你想要买什么,请输入商品编号:")
    if(answer=="q"):
        print("-" * 6 + "购物车" + "-" * 6)
        for item in carts:
            print("%-10s%-5d" % (item[0], item[1]))
        break
    else:
        answer=int(answer)
        if answer>=0 and answer<len(products):
            carts.append(products[answer])
        else:
            break