# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶2
# 利用反射可以导入模块，去模块中找类，根据类创建对象，去对象中寻找对应的值

m = __import__('qz_day15_1', fromlist=True)  # 执行qz_day15_1文件

a = getattr(m, 'C')

b = a('alex')  # 执行qz_day15_1文件中的类C

c = getattr(b, 'n')

print(c)
