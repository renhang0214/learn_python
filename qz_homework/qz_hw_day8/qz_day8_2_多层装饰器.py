# /user/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 装饰器
def outer(func):  # ①
    def inner(*args, **kwargs):  # ②
        print("hello")  # ③
        r = func(*args, **kwargs)  # ④
        print("end")  # ⑤
        return r  # ⑥

    return inner  # ⑦


def outer_1(func):  # ⑧
    def inner(*args, **kwargs):  # ⑨
        print("123")  # ①〇
        r = func(*args, **kwargs)  # ①①
        print("456")  # ①②
        return r  # ①③

    return inner  # ①④


@outer  # ①⑤
@outer_1  # ①⑥
def f1(*args, **kwargs):  # ①⑦
    print("超级复杂！")  # ①⑧


f1(11)  # ①⑨

"""
运行顺序：1 >> 8 >> 15 >> 16 >> 8 >> 9 >> 14 >> 1 >> 2 >> 7 >>
19 >> 2 >> 3 >> 4 >> 9 >> 10 >> 11 >> 15 >> 18 >> 12 >> 13 >> 5 >> 6
"""
