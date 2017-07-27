# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。

def fun(*args):
    print("\n", args,"==>>")
    if not len(args) == 0:
        for i in args:
            i = str(i)
            l = len(i)
            if l == 0:
                print("元素含有空内容\n")
                break
            else:
                pass

    return

s = ""
li = []
tu = (11, 22, 33, 44)
fun(*s)
fun(s)
fun(*li)
fun(*tu)
fun(s, *s, *li, *tu)


