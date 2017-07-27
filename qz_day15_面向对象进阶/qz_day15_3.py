# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶3
# 成员

class P:
    c = 'A'  # 静态字段

    def __init__(self, name):
        temp = 'xxx'
        self.n = name  # 普通字段

    def show(self):  # 类的方法（普通方法）
        print(self.n)

    @staticmethod  # 内置函数：用来装饰类中的方法，使其方法变成静态方法
    def xxx(arg1, arg2):  # 静态方法，静态方法可以无参数
        print('xxx')

    @classmethod  # 内置函数：用来装饰类中的方法，使其方法变成类方法
    def ooo(cls):  # cla为必填参数，执行时会自动将类名传入
        print('ooo')

    def star(self):  # 类的方法（普通方法）
        temp = '%s sb' % self.n
        return temp

    @property  # 内置函数：用来装饰类中的方法，使其方法伪造成字段
    def end(self):
        temp = '%s sb' % self.n
        return temp

    @end.setter  # 用于接收属性（也称特性）
    def end(self, value):
        print(value)
        self.n = value


print(P.c)  # 执行静态字段：类名.静态字段   # 自己访问自己的成员，除了类中的方法

# @staticmethod
P.xxx(1, 2)  # 执行静态方法：类名.方法
# @classmethod
P.ooo()  # 执行类方法：类名.方法

obj = P('alex')
print(obj.star())  # 执行类的方法（普通方法）

# @property
print(obj.end)  # 执行伪造成字段的方法

# @end.setter
obj.end = '123'  # 设置属性（也称特性）
print(obj.end)

