# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶4
# 成员修饰符：用双下划线开头表示私有，仅供内部使用不能被继承

class A:
    x = 'x'  # 普通字段
    __o = '__o'  # 私有字段


    def __init__(self):
        self.__x = '__x'
    def s(self):
        print(self.__o)

class B(A):
    def c(self):
        print(self.__x)
    pass


    # a = B()


print(B.x)
# print(_A__o)  # # 报错，私有字段不能外部访问
# print(B.__o)  # 报错，私有字段不能被继承
A().s()
# print(B().__x)  # 报错，私有字段不能被继承
# B().c()  # 报错，私有字段不能被继承
