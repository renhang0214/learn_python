# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 装饰器
def outer(func):
    def inner():
        print("hello")
        r = func()
        print("end")
        return r

    return inner


@outer
def f1():
    print("F1")


f1()
# hello
# F1
# end
