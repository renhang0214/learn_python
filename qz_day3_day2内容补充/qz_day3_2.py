# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 上节课内容补充2
# 字符串
name = "李璐"

for i in name:
    print(i)  # 循环的每一个字符串是"字符"
    """
    李
    璐
    """
bytes_list = bytes(i, encoding="utf-8")
print(bytes_list)  # 默认每一个字节都是16进制表示
"""
b'\xe7\x92\x90'
"""
for b in bytes_list:
    print(b)  # 默认每一个字节都是10进制表示
    print(bin(b))  # 2进制
    """
    231
    0b11100111
    146
    0b10010010
    144
    0b10010000
    """