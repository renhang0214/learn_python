# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# time模块
import time

# time.sleep(n) 等待n秒
print("1")
time.sleep(1)
print("2")

# time.time()   返回时间戳
print(time.time())

# time.ctime()  返回当前时间的字符串
print(time.ctime())
print(time.ctime(time.time()))  # 返回时间戳的字符串

# time.gmtime(time.time())  分组显示时间的年月日等信息（非本地时间）
print(time.gmtime())

# time.localtime()    分组显示时间的年月日等信息（本地时间）
print(time.localtime())

# time.mktime(time.struct_time时间对象)   将时间对象转换成时间戳
print(time.mktime(time.localtime()))

# time.strftime(格式，time.struct_time时间对象)   将时间对象转换成指定格式的字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# time.strptime(字符串，字符串的格式)    将指定格式的字符串转换成time.struct_time时间对象
print(time.strptime("2016-01-01", "%Y-%m-%d"))

# datetime模块(用法与time模块一样)
import datetime

# datetime.date.today()   以时间格式输出当前日期
# datetime.date.fromtimestamp(time.time())    将时间戳转换为日期格式
# datetime.datetime.now()   以时间格式输出当前时间
# datetime.datetime.now().timetuple()   以time.struct_time时间对象输出当前时间
# datetime.datetime.now().replace(year=2014, hour=12)   替换时间
# datetime.datetime.strptime()    转换日期格式，用法同time模块的的time.strptime一样
# 时间加减法：
# datetime.datetime.now() + datetime.timedelta(3)  # 当前时间+3天
# datetime.datetime.now() + datetime.timedelta(-3)  # 当前时间-3天
# datetime.datetime.now() + datetime.timedelta(hours=3)  # 当前时间+3小时
# datetime.datetime.now() + datetime.timedelta(minutes=30)  # 当前时间+30分