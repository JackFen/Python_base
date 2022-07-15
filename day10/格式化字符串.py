# -*- codeing = utf-8 -*-
# @Time : 2022-07-15 下午 4:41
# @Author : fengzhanwei
# @File : 格式化字符串.py
# @Software : PyCharm

# (1) % 占位符
name='张三'
age=20
print('我叫%s，今年%d岁' %(name,age))

#（2）{}
print('我叫{0},今年{1}岁'.format(name,age))

#(3) f-string
print(f'我叫{name},今年{age}岁')

# 指定字符串的宽度和精度

print('%10d' %99) #10表示宽度
print('%.3f' %3.1415926) #.3表示是小数点后三位
# 同时表示宽度和精度
print('%10.3f' %3.1415926)
print('hellohello')

print('{0:.3}'.format(3.1425926)) #.3表示的是一共是3位数
print('{0:.3f}'.format(3.1425926)) #.3f表示的是3位小数
print('{0:10.3f}'.format(3.1425926)) #同时设置宽度和精度