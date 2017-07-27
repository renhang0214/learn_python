# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶1
# 在子类中执行父类的init方法，查看类的成员
class A:
    def __init__(self):
        print('A的构造方法')
        self.a = '动物'


class B(A):
    def __init__(self):
        print('B的构造方法')
        self.b = '猫'
        # 执行父类的init方法
        super(B, self).__init__()
        A.__init__(self)


# 创建类的对象
c = B()
# 类的对象.__dict__  查看类的成员
print(c.__dict__)


# 以下在qz_day15_2中导入
class C:
    def __init__(self, name):
        print('C的构造方法')
        self.n = name


a = C('alex')
b = a.n
print(b)

