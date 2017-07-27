# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 三目运算（三元运算）
# 1
s1 = int(input("输入数字："))
if s1 == 1:
    name = "alex"
else:
    name = "aric"
print("1:", name)
# 1: alex

# 2
name = "alex" if s1 == 1 else "aric"
print("2:", name)
# 2: alex

# 将1简写成2，为三目运算（三元运算）