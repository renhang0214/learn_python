# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

import time

# 1
while True:
    print("1")
    time.sleep(1)
print("end")
# 2
n1 = True
while n1:
    print("1")
    time.sleep(1)
    n1 = False
# 3
star = 1
flag = True
while flag:
    print(star)
    if star == 10:
        flag = False
    star += 1
    time.sleep(1)
print("end")

# 4
star = 1
while True:
    print(star)
    if star == 10:
        break  # 跳出所有循环,并且不执行break下面的代码
    star += 1
    time.sleep(0.1)
print("end")

# 5
while True:
    print("123")
    break  # 跳出所有循环,并且不执行break下面的代码
    print("456")

# 6
while True:
    print("789")
    time.sleep(0.2)
    continue  # 跳出当前循环并继续下一次循环
    print("000")

