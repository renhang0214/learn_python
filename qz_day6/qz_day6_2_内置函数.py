# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 内置函数：
# 绝对值
a = abs(-1)
print("1.abs ==>> ", a)
# 1.abs ==>>  1

# 循环参数，若每一个都为真，返回True，否则返回False
a = all(["", 11, "jksf"])
print("2.all ==>> ", a)
# 2.all ==>>  False

# 循环参数，若有一个都为真，返回True，否则返回False
a = any(["", 11, "jksf"])
print("3.any ==>> ", a)
# 3.any ==>>  True

# 到对象的类中寻找__repr__方法，获取返回值
class Foo():
    def __repr__(self):
        return "hello"
obj = Foo()
r = ascii(obj)
print("4.obj ==>> ", r)
# 4.obj ==>>  hello

# 二进制
a = bin(10)
print("5.bin ==>> ", a)
# 5.bin ==>>  0b1010

# 八进制
a = oct(10)
print("6.oct ==>> ", a)
# 6.oct ==>>  0o12

# 十进制
a = int(10)
print("7.int ==>> ", a)
# 7.int ==>>  10

# 十六进制
a = hex(10)
print("8.hex ==>> ", a)
# 8.hex ==>>  0xa

# 布尔值，判断真假
a = bool("")
b = bool(" ")
print("9.bool ==>> ", "a:", a, "b:", b)
# 9.bool ==>>  a: False b: True

# 字节
a = bytes("一个", encoding="utf-8")
print("10.bytes ==>> ", a)
# 10.bytes ==>>  b'\xe4\xb8\x80\xe4\xb8\xaa'

#  字节列表
a = bytearray("一个", encoding="utf-8")
print("11.bytearray ==>> ", a)
# 11.bytearray ==>>  bytearray(b'\xe4\xb8\x80\xe4\xb8\xaa')

# 检测能否被执行，调用
def f1():
    pass
f2 = 1223
a = callable(f1())
b = callable(f2)
print("12.callable ==>> ", "a:", a, "b:", b)
# 12.callable ==>>  a: False b: False

"""
# compile()  # 编译
exec()  # 执行Python代码或字符串,接受代码或表达式,无返值
s = "print(123)"
r = compile(s,"<string>","exec")  # 第三位为编译模式,single:单行;eval:表达式;exec:与python一样的代码
print(r)  # <code object <module> at 0x101337ed0, file "<string>", line 1>
# 执行python代码
exec(r)

# eval()  # 执行表达式并获取结果,有返回值,
s = "8*8"
ret = eval(s)
print(ret)  # 64
"""
# dict()  # 字典
# dir()  # 快速查看一个对象提供了哪些功能
# help()  # 快速查看一个对象的帮助信息

# 计算用于得出商，余
a = divmod(10, 3)
print("13.divmod ==>> ", a)
# 13.divmod ==>>  (3, 1)

"""
filter():循环第二个参数里面的每一个元素并执行函数,如果返回值为True,表示元素合法  # 用作筛选,过滤
# 返回值为true,将元素添加到结果中
def f2(a):
    if a > 22:
        return True
list_1 = [11, 22, 33, 44, 55]
ret = filter(f2, list_1)
print(list(ret))
# [33, 44, 55]

上述可写成lambda表达式为:
list_1 = [11, 22, 33, 44, 55]
result = filter(lambda a: a > 22, list_1)
print(list(result))
# [33, 44, 55]
"""

"""
map:(函数,可迭代的对象(即可以for循环的东西))  # 数据等批量处理
# 将函数返回值添加到结果中
li = [11, 22, 33, 44, 55]
def f1(a):
    return a + 100
result = map(f1,li)
print(list(result))
# [111, 122, 133, 144, 155]

# 上述可写成lambda表达式为:
li = [11, 22, 33, 44, 55]
result = map(lambda a: a + 100, li)
print(list(result))
# [111, 122, 133, 144, 155]
"""

# frozenset    等同于冻结的set
# globals    获取全局变量
# locals    获取局部变量
# hash    用于Python内部，获取字典key的hash值，可以快速找到，占用内存小
# id    查看内存地址
# input    等待用户输入
# int    强制转换为整数（默认十进制）
# isinstance    查看某一个对象是否为另一个对象的实例
# issubclass    查看某一个类是否为另一个类的派生类(子类)

# iter    创建一个可以被迭代的对象
# next    取迭代的值
obj = iter([11, 22, 33, 44])
print("14.iter ==>> ", obj)
# 14.iter ==>>  <list_iterator object at 0x102079c50>
r = next(obj)
print("15.next ==>> ", r)
# 15.next ==>>  11

# len    查看长度:Python2+中按照字节计算;Python3+中按照字符计算
# list    返回列表
# max    求最大值
# min    求最小值
# sum()  # 求和
# memoryview    类:与内存地址相关
# object    类:所有类的副类
# open    对文件进行操作
# ord    把一个字符串表示的字符转换为字符相对应的整数，适用于UNICODE字符
# pow     求指数:平方,次方等
# print    输出结果
# range    范围
# repr    执行类中的__repr__方法
# reversed    反转
# round    四舍五入
# set    集合
# slice     切片
# sorted     排序（执行类内部的sort方法）
# str    字符串
# tuple    元组
# type    类型
# vars    获取当前模块可使用变量

# zip()
# 1
l1 = ["I", 11, 22, 33]
l2 = ["am", 44, 55, 66]
l3 = ["R.H", 77, 88, 99]
r = zip(l1, l2, l3)
temp = list(r)[0]
ret = " ".join(temp)
print("16.zip ==>> ", "r:", r, "ret:", ret)
# 16.zip ==>>  I am R.H
# 2
l1 = ["I", 11, 22, 33]
l2 = ["am", 44, 55, 66]
l3 = ["R.H", 77, 88, 99]
r = zip(l1, l2, l3)
l = []
for i in r:
    l.append(i)
print("16.zip ==>> ", l)
# 16.zip ==>>  [('I', 'am', 'R.H'), (11, 44, 77), (22, 55, 88), (33, 66, 99)]















