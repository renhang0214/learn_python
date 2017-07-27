# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 功能
se = {11, 22, 33}
print("se==>>", se)
# se==>> {33, 11, 22}
# 新增
se.add(44)
print("add==>>", se)
# add==>> {33, 11, 44, 22}

# 清除
se.clear()
print("clear==>>", se)
# clear==>> set()

se = {11, 22, 33, 44}
be = {22, 55}
# se有，be没有
ret = se.difference(be)
print("se==>>", se, "difference==>>", ret)
# se==>> {33, 11, 44, 22} difference==>> {33, 11, 44}
# se有，be没有，更新se（删除相同的）
ret = se.difference_update(be)
print("se==>>", se, "difference_update==>>", ret)
# se==>> {33, 11, 44} difference_update==>> None

se = {11, 22, 33, 44}
be = {22, 55}
# 找交集
ret = se.intersection(be)
print("se==>>", se, "intersection==>>", ret)
# se==>> {33, 11, 44, 22} intersection==>> {22}
# 找到交集并更新到se
ret = se.intersection_update(be)
print("se==>>", se, "intersection_update==>>", ret)
# se==>> {33, 11, 44, 22} intersection_update==>> None

# 判断有无交集，有交集返回False，无交集返回True
ret = se.isdisjoint(be)
print("isdisjoint==>>", ret)
# isdisjoint==>> False

# 判断se是否为be的子序列，是返回True，不是返回False
ret = se.issubset(be)
print("issubset==>>", ret)
# issubset==>> False
# 判断se是否为be的父序列，是返回True，不是返回False
ret = se.issuperset(be)
print("issuperst==>>", ret)
# issuperst==>> False

se = {11, 22, 33, 44}
# 移除元素并重新赋值(随机)
ret = se.pop()
print("se==>>", se, "pop==>>", ret)
# se==>> {11, 44, 22} pop==>> 33

se = {11, 22, 33, 44}
be = {22, 55, 77, 33}
# 找se中有be中没有,找be中有se中没有，并赋值给新的变量
ret = se.symmetric_difference(be)
print("se==>>", se, "symmetric_difference==>>", ret)
# se==>> {33, 11, 44, 22} symmetric_difference==>> {11, 44, 77, 55}
# 找se中有be中没有,找be中有se中没有，并赋更新到se
ret = se.symmetric_difference_update(be)
print("se==>>", se, "symmetric_difference_update==>>", ret)
# se==>> {11, 44, 77, 55} symmetric_difference_update==>> None

# 并集
ret = se.union(be)
print("se==>>", se, "be==>>", be, "union==>>", ret)
# se==>> {11, 44, 77, 55} be==>> {33, 77, 22, 55} union==>> {33, 11, 44, 77, 22, 55}

# 把be更新到se，be也可以是列表,元组
ret = se.update(be)
print("se==>>", se, "be==>>", be, "update==>>", ret)
# se==>> {33, 11, 44, 77, 22, 55} be==>> {33, 77, 22, 55} update None

# 删除指定元素，不存在不报错
se.discard(55)
print("discard==>>", se)
# discard==>> {33, 11, 44, 77, 22}
# 删除指定元素，不存在报错
se.remove(55)
print("remove", se)
# KeyError: 55(报错）



