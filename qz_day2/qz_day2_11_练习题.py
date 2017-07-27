# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 练习题
# 1、for循环
# 用户按照顺序循环可迭代对象中的内容，
# PS：break、continue
li = [11, 22, 33, 44]
for item in li:
    print(item)

# 2、enumrate
# 为可迭代的对象添加序号
li = [11, 22, 33]
for k, v in enumerate(li, 1):
    print(k, v)
# 3、range和xrange
# 指定范围，生成指定的数字
print(range(1, 10))

for i in range(1, 10):
    print(i)
    # 结果：[1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 10, 2):
    print(i)
    # 结果：[1, 3, 5, 7, 9]

for i in range(30, 0, -2):
    print(i)
    # 结果：[30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
