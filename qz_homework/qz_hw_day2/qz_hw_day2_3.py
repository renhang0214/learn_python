# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 输出商品列表，用户输入序号，显示用户选中的商品

li = ["手机", "电脑", '鼠标垫', '游艇']

for k, v in enumerate(li):  # 循环li,并为元素添加序号
    print(k, v)  # 输出序号和li内元素
b = input("请输入商品序号:")  # 输入元素序号
if b.isdigit():
    b = int(b)
    if b < len(li):
        print(li[b])  # 输出序号对应的元素
    else:
        print("输入错误!")
else:
    print("输入错误。")
