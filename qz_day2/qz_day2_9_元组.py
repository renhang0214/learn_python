# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang


# 元组
name_tuple = ("alex", "eric")
# 索引
print(name_tuple[0])
# len
print(name_tuple[len(name_tuple)-1])
# 切片
print(name_tuple[0:1])
# for
for i in name_tuple:
    print(i)
# 删除
# del name_tuple[0] 不支持
# count 计算个数
print(name_tuple.count("alex"))
# index 获取指定元素的索引位置
print(name_tuple.index("alex"))
