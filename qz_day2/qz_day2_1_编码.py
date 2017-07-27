# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 编码
"""
#2.7

temp = "李杰"  # utf-8
# 解码,需要解释原来所用编码
temp_unicod = temp.decode('utf-8')
temp_gbk = temp_unicod.encode("gbk")
print(temp_gbk)
"""

# 3.+

temp = "李杰"
temp_gbk = temp.encode("gbk")
print(temp_gbk)

