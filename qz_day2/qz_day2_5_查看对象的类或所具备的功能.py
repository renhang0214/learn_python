# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 查看对象的类或所具备的功能
# 1
temp = "hey"
t = type(temp)  # 数据类型
print(t)  # <class 'str'>
# str,ctr+鼠标左键,找到str类,内部所有的方法
# 2
temp = "Alex"
t = dir(temp)  # 获取数据类型
print(t)  # <获取  '>
# 3
t = help(type(temp))
print(t)
# 4
# 直接点击:鼠标直接放在要查询的功能上,(MAC版)command+左键,直接定位到功能处