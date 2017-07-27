# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 5、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def func(*args):
    l = len(args)
    new_li = []
    if l <= 2:
        args = list(args)
        print(args)
    else:
        new_li = args[0:2]
        new_li = list(new_li)
        print(new_li)

l1 = [1111, 22, 33, "sdjkh"]
l2 = ["dkjshd", 11]

func(*l1)
func(*l2)