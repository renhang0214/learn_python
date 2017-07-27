# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang
# 字符串
a = "ren hang"
ret = a.capitalize()
print(ret)

a = "ren hang"
ret = a.center(20, "*")
print(ret)

a = "alex ren gill"
b = a.count("l")
print(b)
# 3

a = "alex"
b = a.endswith("x")
print(b)

a = "ren\thang"
b = a.expandtabs()
b2 = a.expandtabs(20)
print(b, b2)

a = "ren hang"
b = a.find("a")
b2 = a.index("n")
print(b, b2)

a = "hello {0}, age {1}"
b = a.format("alex", 26)
print(b)

a1 = "renhang0214"
a2 = "renhang"
b1 = a1.isalnum()
b2 = a2.isalnum()
print(b1, b2)

a1 = "renhang0214"
a2 = "renhang"
b1 = a1.isalpha()
b2 = a2.isalpha()
print(b1, b2)

a1 = "renhang0214"
a2 = "1234"
b1 = a1.isdigit()
b2 = a2.isdigit()
print(b1, b2)

a1 = "renhang0214"
a2 = "1234"
b1 = a1.islower()
b2 = a2.islower()
print(b1, b2)

a1 = "ren hang"
a2 = "renhang"
a3 = " "
b1 = a1.isspace()
b1 = a2.isspace()
b3 = a3.isspace()
print(b1, b2, b3)

a1 = "Ren Hang"
a2 = "ren Hang"
b1 = a1.istitle()
b2 = a2.istitle()
print(b1, b2)

a1 = "Ren Hang"
a2 = "REN HANG"
b1 = a1.isupper()
b2 = a2.isupper()
print(b1, b2)

a = ["abc", "alex"]
b = "_".join(a)
print(b)

a = "Grissom"
b = a.ljust(15, "=")
print(b)

a = "REN"
b = a.lower()
print(b)

a = "      Grissom"
b = a.lstrip()
print(b)

a = "gissom 123 ren hang"
b = a.partition("123")
print(b)

a = "gissom 123 ren hang"
b = a.replace("g", "G", 1)
print(b)

a = "gissom gil ren hang"
b1 = a.rsplit("g")
b2 = a.rsplit("g", 2)
print(b1, b2)

a = "gissom gil ren hang  "
b = a.rstrip()
print(b)

a = "gissom gil ren hang"
b = a.split("g")
print(b)

a = "gil\ngissom"
b = a.splitlines()
print(b)

a = "gissom"
b = a.startswith("g")
print(b)

a = "  gissom  "
b = a.strip()
print(b)

a = "gISSOm"
b = a.swapcase()
print(b)

a = "gissom"
b = a.title()
print(b)

a = "gissom"
b = a.upper()
print(b)

a = "grissom"
b = a.zfill(20)
print(b)

# 切片
a = "grissom"
b = a[0:2]
print(b)

# 输出字符串长度
a = "gissom 123"
b = len(a)
print(b)

a = "grissom"
# while 循环
star = 0
while star < len(a):
    temp = a[star]
    print(temp)
    star += 1

# for 循环
for item in a:
    print(item)

for item in a:
    if item == "s":
        continue
    print(item)

for item in a:
    if item == "s":
        break
    print(item)

