# /user/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 单层装饰器
def outer(func):  # ①
    def inner(*args, **kwargs):  # ②
        print("hello")  # ③
        r = func(*args, **kwargs)  # ④
        print("end")  # ⑤
        return r  # ⑥

    return inner  # ⑦


# def outer_1(func):  # ⑧
#     def inner(*args, **kwargs):  # ⑨
#         print("123")  # ①〇
#         r = func(*args, **kwargs)  # ①①
#         print("456")  # ①②
#         return r  # ①③
#
#     return inner  # ①④


@outer  # ①⑤
# @outer_1  # ①⑥
def f1(*args, **kwargs):  # ①⑦
    print("超级复杂！")  # ①⑧


f1(11)  # ①⑨


# 运行顺序：1 >> 15 >> 1 >> 2 >> 7 >> 19 >> 2 >> 3 >> 4 >> 15 >> 18 >> 5 >> 6

"""
代码从上往下依次运行 1 >> 15 >> 1 >> 2 >> 7 >> 19
19 ：运行f1函数，f1可以是任意参数 >> 2
2：因为函数f1上加上了装饰器outer，运行outer内的inner函数 >> 3  >> 4
4：因为outer为装饰器，装饰器加在f1上，所以f1函数作为outer的参数，r = func（）相当于r = f1（），执行f1函数内的代码 >> 15 >> 18 >> 5 >> 6

上面的代码，相当于下面的代码，

"""


def inner(*args, **kwargs):  # ②
    print("hello")  # ③

    r = print("超级复杂！")  # ①⑧

    print("end")  # ⑤

    # return r  # ⑥


inner()
