# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 上节课内容补充1
# 类：举例
class MyInt(object):
    def __init__(self):
        print("init")
    def __call__(self, *args, **kwargs):
        print("ok")

obj = MyInt()
# 输出结果：init
obj()
# 输出结果：0k
