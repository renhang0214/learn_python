# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang


def f1():
    return "f1"


def f2():
    r = f1()
    return r


def f3():
    r = f2()
    return r


def f4():
    r = f3()
    return r


print(f4())  # f1


# 斐波那契函数：
def func(a1, a2, n):
    a3 = a1 + a2
    if n == 10:
        return a2
    return func(a2, a3, n + 1)


print(func(0, 1, 1))
