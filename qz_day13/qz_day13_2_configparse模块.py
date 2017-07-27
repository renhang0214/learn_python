# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import configparser

c = configparser.ConfigParser()

# resd(文件名)打开并读取文件
c.read("c1", encoding="utf-8")

# sections()获取所有的节点
a = c.sections()
print(a)

# options(节点名)获取节点的键值
a = c.options("section1")
print(a)

# items(节点名)获取节点的键值对
a = c.items("section1")
print(a)

# get(节点名, 键值)获取节点中键值的值；
# getint(节点名, 键值)获取节点中键值的值并转换为整型；
# getfloat(节点名, 键值)获取节点中键值的值并转换为浮点型；
# getboolean(节点名, 键值)获取节点中键值的值并转换为布尔型；
a = c.get("section1", "k1")
print(a)

# has_section(节点名)判断是节点是否存在
a = c.has_section("section1")
print(a)

# add_section(节点名)添加节点
c.add_section("section3")
print(c.sections())

# c.remove_section(节点名)删除节点
c.remove_section("section3")
print(c.sections())

# has_option(节点名, 键值)判断是节点的键值是否存在
a = c.has_option("section1", "k1")
print(a)

# c.remove_option(节点名, 键值)删除节点的键值
c.remove_option("section1", "k1")
print(c.options("section1"))

# c.set(节点名, 键值, 值)判断节点内键值的值是否存在，不存在创建，存在则更改
c.set("section1", "k1", "456")
c.set("section2", "k1", "123")
print(c.get("section1", "k1"))
print(c.get("section2", "k1"))

# c.write(open(文件名, 打开方式))写入文件，文件名存在对原文件进行更改，文件不存在创建
c.write(open("c2", "w"))
