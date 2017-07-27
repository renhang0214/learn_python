# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 练习：随机验证码
import random

temp = ""

for i in range(6):
    # 生成0-9的随机数
    num = random.randrange(0, 10)
    # 生成的数字为3或者7的时候
    if num == 3 or num == 7:
        # 生成0 - 9的随机数
        rad1 = random.randrange(0, 10)
        # 将随机数转换成字符串
        c1 = str(rad1)
        temp += c1
    else:  # 否则
        # 生成65-90的随机数
        rad2 = random.randrange(65, 91)
        # 将随机数转换成大写字母
        c2 = chr(rad2)
        temp += c2

print(temp)
