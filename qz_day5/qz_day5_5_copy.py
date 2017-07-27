# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

import copy

# 数字、字符串
n1 = 123
# n1 = "i am alex age 10"
print(id(n1))
# 赋值：id不变
n2 = n1
print(id(n2))
# 浅拷贝：id不变
n2 = copy.copy(n1)
print(id(n2))
# 深拷贝：id不变
n3 = copy.deepcopy(n1)
print(id(n3))

# 其他数据类型
n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
# 赋值：id不变
n2 = n1
# 浅拷贝：最外层id改变，里层id不变
n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
n3 = copy.copy(n1)
# 深拷贝：外层id改变，最里层id不变
n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
n4 = copy.deepcopy(n1)