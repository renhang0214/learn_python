# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 6、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#

def fun(*args):
    l = len(args)
    # print(l)
    new_li = []
    for i in range(l):
        # print(i)
        if i % 2 == 1:
            new_i = str(args[i])
            new_li.append(args[i])
    # print(new_li)
    return (new_li)


li = ["hsjh", 11, 22, "nsdjf"]
tu = ("hsjh", 11, 22, "nsdjf")

r1 = fun(*li)
print("li:", r1)
r2 = fun(*tu)
print("tu:", r2)
