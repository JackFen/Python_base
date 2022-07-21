# -*- codeing = utf-8 -*-
# @Time : 2022-07-21 上午 11:28
# @Author : fengzhanwei
# @File : 第三方模块的安装.py
# @Software : PyCharm

# 在cmd 输入pip install 模块名
# 安装完成后，输入python,import 模块名 不报错的话，说明安装成功
import schedule
import time
def job():
    print('haha----')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)