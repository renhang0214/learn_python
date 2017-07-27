# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 反射：根据字符串去某个对象中去操作其成员
# 正常导入模块 ==>>   import 模块名 as 重新起名
# 根据用户输入的内容导入模块
# 重新起名 = __import__(模块名)


# from xml.etree import ElementTree as ET
# ET = __import__("xml.etree.ElementTree", fromlist=True)
# 参数fromlist=True：像上面示例中的模块导入时需要加此参数

# from lib.account import a as abc
#
# b = abc.login()
# print(b)

s1 = input("shuru1:")
s2 = input("shuru2:")
abc = __import__(s1, fromlist=True)
nb = getattr(abc, s2)
nb1 = nb()
print(nb1)

# # 模拟web框架
# from lib.account import a
# url = input("shuru：")
# inp = url.split('/')[-1]
# if hasattr(a, inp):
#     target_func = getattr(a, inp)
#     r = target_func()
#     print(r)
# else:
#     print("404")
