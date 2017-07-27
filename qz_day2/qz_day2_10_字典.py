# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang
# 字典
user_info = {
    "name": "alex",
    "age": 20,
    "gender": "M"
}
# 索引 通过key进行(取值时,key不存在,报错)
print("1", user_info["name"])
# 循环
for i in user_info:
    print("2", i)
# 获取所有的键
print("3", user_info.keys())
# 获取所有的值
print("4", user_info.values())
# 获取所有的键值对
print("5", user_info.items())
for k, v in user_info.items():
    print("6", k, v)
# get 根据key获取值,如果key不存在,可以指定一个默认值
val = user_info.get("name")
print("7", val)
val2 = user_info.get("user", "gr")
print("8", val2)
# 检查字典中某个key是否存在 《2.7版本》
# 更新
t = {"a1": 123, "a2": 456}
user_info.update(t)
print("9", user_info)
# 删除指定的键值对
del user_info["a1"]
print("10", user_info)
# clear 清除所有内容
user_info.clear()
print("11", user_info)
