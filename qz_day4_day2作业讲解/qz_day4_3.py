# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 三、输出商品列表，用户输入序号，显示用户选中的商品
li = ["手机", "电脑", '鼠标垫', '游艇']

# 方法1
while True:
    for i, j in enumerate(li):
        print(i+1, j)
    num = input("num:")
    if num.isdigit():
        num = int(num)
        if 0 < num < len(li):
            print(li[num-1])
            break
        else:
            print("输入错误！请输入商品对应的编号:")
    else:
        print("输入错误！请输入商品对应的编号:")




