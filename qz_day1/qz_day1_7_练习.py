# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 1.使用while循环输入 1 2 3 4 5 6     8 9 10

num = 1

while True:
    if num == 7:
        num += 1
        continue
    print(num)
    if num == 10:
        break
    num += 1


# 2、求1-100的所有数的和

num = 1
num_sum = 0
while True:
    print(num)
    num_sum = num_sum + num
    if num == 100:
        break
    num += 1

print(num_sum)