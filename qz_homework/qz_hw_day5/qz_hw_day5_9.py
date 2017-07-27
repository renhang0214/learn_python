# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 非递归
def func():
    li = []
    n = ""
    for i in range(10):
        if i == 0:
            li.append(1)
        elif i == 1:
            li.append(1)
        else:
            n = li[i-1] + li[i-2]
            # print(n)
            li.append(n)
    print(li[10-1])
    return

func()

# 递归
def func(a1, a2, n):
    a3 = a1 + a2
    if n == 10:
        return a2
    return func(a2, a3, n + 1)


print(func(0, 1, 1))

