# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象：不是所有的情况都适用
# c#、java只能用面向对象进行编程，Python即可以用函数编程也可以用面向对象编程
# 函数编程比较繁琐，面向对象比较方便

# 面向对象编程过程
# 创建类（用于封装函数）
class xxx:
    def f1(self):
        print("f1")

    def f2(self):
        print("f2")

    def f3(self):
        print("f3")

    def f4(self):
        print("f4")


# 根据类创建对象，使用对象去执行类中的方法
a = xxx()
b = a.f1()


# 封装
# 方法1
class ooo:
    def o1(self):
        print(self.b1)

    def o2(self):
        print(self.b1)


obj1 = ooo()  # 创建对象
obj1.b1 = "abc"  # 在对象中封装数据
obj1.o1()  # 执行类的方法，在执行过程中可以根据self去obj1中去提取封装里面的数据

obj2 = ooo()
obj2.b1 = "xxx"
obj2.o2()


# 方法2：__init__构造方法
# 通过对象直接调用
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj1 = Foo("ooo", 18)
print(obj1.name, obj1.age)
obj2 = Foo("xxx", 19)
print(obj2.name, obj2.age)


# 通过self间接调用
class Foo:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def fo(self):
        print(self.n)
        print(self.a)


obj1 = Foo("ooo", 18)
obj1.fo()
obj2 = Foo("xxx", 19)
obj2.fo()


# 继承
class Animals:  # 基类
    def chi(self):
        print("吃")

    def he(self):
        print("喝")


class Dog(Animals):  # 派生类
    def __init__(self, name):
        self.na = name

    def jiao(self):
        print(self.na + "wang")


a = Dog("wangwnag")  # 创建派生类对象
a.chi()  # 执行基类方法
a.he()
a.jiao()

# 多态：多种形态。Python本身支持多态
class Foo:
    def f1(self):
        print("Foo")


class Bar:
    def f1(self):
        print("Bar")


def func(arg):
    arg.f1()


func(Foo())
func(Bar())


# 接口：Java、c#等其他语言（首字母为I）
# 在Python中默认不存在，用于约束，不能实现任何功能，如果派生类继承接口则派生类必须实现接口内的每一个功能
