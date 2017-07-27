# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


"""
迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退，不过这也没什么，因为人们很少在迭代途中往后退。另外，迭代器的一大优点是不要求事先准备好整个迭代过程中所有的元素。迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后，元素可以不存在或者被销毁。这个特点使得它特别适合用于遍历一些巨大的或是无限的集合，比如几个G的文件

特点：

访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
不能随机访问集合中的某个值 ，只能从头到尾依次访问
访问到一半时不能往回退
便于循环比较大的数据集合，节省内存
"""
# 用迭代器实现range
def range(num):
    temp = -1
    while True:
        temp = temp + 1
        if temp >= num:
            return
        else:
            yield temp


for i in range(5):
    print(i)
'''
a = range(5)
b = a.__next__()
print(b)  # 0
b = a.__next__()
print(b)  # 1
b = a.__next__()
print(b)  # 2
b = a.__next__()
print(b)  # 3
b = a.__next__()
print(b)  # 5
'''