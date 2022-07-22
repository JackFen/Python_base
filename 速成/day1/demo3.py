# -*- codeing = utf-8 -*-
# @Time : 2022/4/19 下午 10:01
# @Author : fengzhanwei
# @File : demo3.py
# @Software : PyCharm

#if True:
#if 0:
''''
if False:         #错误的多条语句
    print("True")
  print("Answer")
'''

'''
if True:
    print("True") #python通过语句缩进来判断是否属于同一结构
    print("Answer")#即if里面的语句前面的空格必须相同（一般为4个即一个制表符）
else:
    print("False")
print("end")
'''

'''
score=87

if score>=90 and score<=100:
    print("本次考试等级为A")
elif score>=80 and score<90:
    print("本次考试等级为B")
elif score>=70 and score<80:
    print("本次考试等级为C")
elif score>=60 and score<70:
    print("本次考试等级为D")
else:
    print("本次考试等级为E")    #else不一定为最后一个，最后一个也可以为elif
'''

'''
xingBie=1
danshen=1
if xingBie==1:
    print("男生")
    if danshen==1:
        print("单身")
    else:
        print("不是单身")
else:
    print("女生")
'''
'''
import random #引入随机库

x=random.randint(0,2) #随机生成【0,2】的随机数，包含0,1,2三个数字

print(x)
'''

#小作业 石头剪子布
import random
b = random.randint(0, 2)
a=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
print("随机生成的数字为%d"%b)
if a>=0 or a<=2:
    if a-b==-1 or a-b==2:
        print("哈哈，你输了:)")
    elif a-b==0:
        print("平局")
    else:
        print("你赢了")
else:
    print("你输的数字不对哦")