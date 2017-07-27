# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

name = "alex"
age = 18
# 列表
name_list = ["alex", "eric", "gill"]
print(name_list)
# 索引
print(name_list[0])
# 切片
print(name_list[0:2])
# len
print(name_list[2:len(name_list)])
# for
for i in name_list:
    print(i)
# 追加
name_list.append("R")
print(name_list)
# 统计
b = name_list.count("alex")
print(b)
# 扩充
temp = [11, 22, 33]
name_list.extend(temp)
print(name_list)
# 索引
b = name_list.index("alex")
print(b)
# 插入
b = name_list.insert(2, "grissom")
print(name_list)
# 在原列表移除最后一个元素并赋值给其他变量（可仅移除）
b = name_list.pop()
print(name_list)
print(b)
# 删除某个元素
name_list.remove(11)
print(name_list)
# 反转
name_list.reverse()
print(name_list)
# del 删除
del name_list[1]
print(name_list)
# del 删除指定索引位置
del name_list[1:3]
print(name_list)
