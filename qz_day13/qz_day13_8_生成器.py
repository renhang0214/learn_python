# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

# 生成器
def func():
    yield 1
    yield 2
    yield 3
    yield 4


a = func()

b = a.__next__()
print(b)  # 1

b = a.__next__()
print(b)  # 2

b = a.__next__()
print(b)  # 3

b = a.__next__()
print(b)  # 4


# 用生成器实现xrange
def xrange(num):
    temp = -1
    while True:
        temp = temp + 1
        if temp >= num:
            return
        else:
            yield temp

a = xrange(5)

b = a.__next__()
print(b)  # 0
b = a.__next__()
print(b)  # 1
b = a.__next__()
print(b)  # 2
b = a.__next__()
print(b)  # 3
b = a.__next__()
print(b)  # 5
