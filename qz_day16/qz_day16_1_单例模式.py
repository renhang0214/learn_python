# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 单例模式
class P:
    def __init__(self):
        self.name = 'xxx'
        self.age = 'xx'

    def f1(self):
        print (self.name, self.age)
        pass


xx = P()
xx.f1()
