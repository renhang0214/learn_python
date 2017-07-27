# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 5、求1-2+3-4+5 ... 99的所有数的和

num = 1
a = 0
b = 0
sum_num = 0
while True:
    if num == 100:  # 判断num=100
        break  # 跳出循环
    if num % 2 == 1:
        a = a + num
        num += 1
        # print(a)
    else:
        b = b + num
        num += 1
        print(b)
    num_sum = a - b  # a-b+a-b+...+a
print(num_sum)