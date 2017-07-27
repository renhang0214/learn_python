# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 上节课内容补充4
# 字典

# 创建
a1 = {"k1": 123}
print(1, a1)
# {'k1': 123}

a2 = dict(k1=123, k2=456)
print(2, a2)
# {'k1': 123, 'k2': 456}

li = [11, 22, 33]
new_dict = dict(enumerate(li))
print(3, new_dict)
# {0: 11, 1: 22, 2: 33}

# 特殊功能
dic = {"k1": 11, "k2": 22, "k3": 33, "k4": 44}
n = dict.fromkeys(["k1", "k2", "k3"], "alex")
print(4, n)
# {'k1': 'alex', 'k3': 'alex', 'k2': 'alex'}

n1 = dict.fromkeys(["k1", "k2", "k3"], [])
n1["k1"].append("x")
print(5, n1)
# {'k1': ['x'], 'k2': ['x'], 'k3': ['x']}

n2 = {'k1': [], 'k2': [], 'k3': []}
n2["k1"].append("x")
print(6, n2)
# {'k1': ['x'], 'k2': [], 'k3': []}
