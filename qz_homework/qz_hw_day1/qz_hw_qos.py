# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 4、输出 1-100 内的所有偶数

num = 1

while True:  # 开始循环

    if num == 100:  # 判断 num
        break  # 跳出所有循环
    remainder = num % 2  # 求num的余数
    if remainder == 0:  # 判断余数
        print(num)  # 输出符合条件的num
        num += 1  # 加1
    else:
        num += 1  # 加1
        continue  # 跳出本次循环