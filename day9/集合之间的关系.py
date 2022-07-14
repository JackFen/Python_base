# -*- codeing = utf-8 -*-
# @Time : 2022-07-14 下午 9:03
# @Author : fengzhanwei
# @File : 集合之间的关系.py
# @Software : PyCharm
'''两个集合是否相等'''
s={10,20,30,40}
s2={30,40,20,10}
print(s==s2) #True
print(s!=s2) #False

'''一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1)) #True
print(s3.issubset(s1)) #False

'''一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2)) #True
print(s1.issuperset(s3)) #False

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3)) #False 两者有交集
