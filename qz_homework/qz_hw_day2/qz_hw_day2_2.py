# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

"""
查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
"""
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
# 循环li
for i in li:
    b = i.strip()  # 去除空格
    # print(b)
    if b.startswith("a") and b.endswith("c"):  # 判断以a开头以c结束的元素
        print("1", b)  # 输出元素
    elif b.startswith("A") and b.endswith("c"):  # 判断以A开头以c结束的元素
        print("2", b)  # 输出元素
# 循环tu
for i in tu:
    b = i.strip()  # 去除空格
    # print(b)
    if b.startswith("a") and b.endswith("c"):  # 判断以a开头以c结束的元素
        print("3", b)   # 输出元素
    elif b.startswith("A") and b.endswith("c"):  # 判断以A开头以c结束的元素
        print("4", b)  # 输出元素
# 循环dic
for k, v in dic.items():
    b1 = k.strip()  # 去除空格
    b2 = v.strip()  # 去除空格
    if b1.startswith("a") and b1.endswith("c"):  # 判断以a开头以c结束的元素
        print("5", b1)  # 输出元素
    elif b1.startswith("A") and b1.endswith("c"):  # 判断以A开头以c结束的元素
        print("6",b1)  # 输出元素
    elif b2.startswith("a") and b2.endswith("c"):  # 判断以a开头以c结束的元素
        print("7", b2)  # 输出元素
    elif b2.startswith("A") and b2.endswith("c"):  # 判断以A开头以c结束的元素
        print("8", b2)  # 输出元素
