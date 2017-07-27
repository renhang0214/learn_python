# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def fun(*args):
    print(args)
    l = len(args)
    if l > 5:
        print("大于")
    else:
        print("小于")
    return
s = "jkwefweb"
li = [11, 22, 33, 44]
tu = (11, 22, 33, 44)
fun(s)
fun(*s)
fun(*li)
fun(*tu)
fun(s, *s, *li, *tu)

