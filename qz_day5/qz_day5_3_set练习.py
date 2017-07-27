# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 练习:相同的key更新，old_dict有new_dict没有的key删除，old_dict没有new_dict有的key更新到old_dict
# 数据库中原有
old_dict = {
    "#1": 11,
    "#2": 22,
    "#3": 100
}

# cmdb 新汇报的数据
new_dict = {
    "#1": 33,
    "#3": 22,
    "#4": 100
}

old_set = set(old_dict.keys())
new_set = set(new_dict.keys())

# 需要更新的key
update_key = old_set.intersection(new_set)
# 需要删除的key
del_set = old_set.difference(new_set)
# 需要新增的key
add_set = new_set.difference(old_set)

# 相同的key更新
for up_i in update_key:
    for i2 in new_dict.keys():
        if i2 == up_i:
            up_ret = {i2: new_dict[i2]}
            # print(ret)
            old_dict.update(up_ret)

# old_dict有new_dict没有的key删除
for del_i in del_set:
    # print(del_i)
    del old_dict[del_i]

# old_dict没有new_dict有的key更新到old_dict
for ad_i in add_set:
    ad_ret = {ad_i: new_dict[ad_i]}
    # old_dict.get()
    old_dict.update(ad_ret)
    # print(ad_ret)

print(old_dict)




