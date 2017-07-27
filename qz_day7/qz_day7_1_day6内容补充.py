# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 上节内容补充
# 函数名可以当作参数进行传递
def f1():
    return "F1"


def f2(arg):
    # print(arg)
    return "F2"


x = 123
print("f1:", f1())
# f1: F1
print("f2(x):", f2(x))
# f2(x): F2
print("f2(f1):", f2(f1))


# f2(f1): F2


# 实现筛选功能等同于fillter
def MyFillter(func, seq):
    result = []
    for i in seq:
        ret = func(i)
        if ret:
            result.append(i)
    return result


def f1(x):
    if x > 22:
        return True
    else:
        return False


r = MyFillter(f1, [11, 22, 33, 44])
print("MyFillter:", r)
# MyFillter: [33, 44]

# 实现筛选功能等同于map
li = [11, 22, 33, 44]


def x(arg):
    return arg + 100


def MyMap(func, arg):
    result = []
    for i in arg:
        ret = func(i)
        result.append(ret)
    return result


r = MyMap(x, li)
print("MyMap:", r)
# MyMap: [111, 122, 133, 144]
