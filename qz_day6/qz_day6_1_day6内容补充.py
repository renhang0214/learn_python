# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 补充
# if isinstance(变量名， 数据类型)   判断变量为什么数据类型

# lambda 表达式：可以写简单的函数，f1 = f2, f3 = f4
def f1():
    return 123
print(f1, f1())
# <function f1 at 0x10217c950> 123
f2 = lambda: 123
print(f2, f2())
# <function <lambda> at 0x10217c9d8> 123

def f3(a1, a2):
    return a1 + a2
print(f3, f3(1, 2))
# <function f3 at 0x10217ca60> 3
f4 = lambda a1, a2: a1 + a2
print(f4, f4(1, 2))
# <function <lambda> at 0x10217cae8> 3

