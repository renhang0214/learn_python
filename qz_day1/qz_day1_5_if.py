# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

"""
if 条件:
    代码块
else:
    代码块
"""

if 1 == 1:
    print("11")
else:
    print("22")

if 1 != 1:
    print("111")
else:
    print("222")

if False:
    print("1111")
else:
    print("2222")

if 1 < 2:
    print("Yes")
else:
    print("No")


n1 = 1
n2 = 2
if n1 < n2:
    print("Yes")
else:
    print("No")


name = input("name:")
if name == "renhang":
    print("Yes")
else:
    print("No")


user = input("username:")
pwd = input("password:")
if user == "renhang" and pwd == "123":
    print("Yes")
else:
    print("No")

"""
if 条件:
    代码块
elif 条件:
    代码块
...
else:
    代码块
"""
age = input("Age:")
if age == "1":
    print("1")
elif age == "2":
    print("2")
elif age == "3":
    print("3")
else:
    print("4")


"""
条件:
     True      False
     a > b      a < b    a == b
     a == “变量" or a == “变量"
     a !== “变量"
     a == "变量" and b == "变量"
"""

user = input("username:")
pwd = input("password:")
code = input("code:")

if user == "renhang" and pwd == "123" and code == "123456":
    print("Yes")
else:
    print("No")

if user == "renhang" or user == "alex":
    print("Yes")
else:
    print("No")