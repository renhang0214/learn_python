# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import pickle, json

# pickle.dumps(转换的对象)     将指定的对象转换成字节
# 直接转换
d = {1: "11", 2: "22"}
a = pickle.dumps(d)
print(a)  # b'\x80\x03}q\x00(K\x01X\x02\x00\x00\x0011q\x01K\x02X\x02\x00\x00\x0022q\x02u.'
# 文件操作
f = open("db.txt", "wb")  # 打开文件时要用"字节"方式打开
f.write(pickle.dumps(d))
f.close()

# pickle.dump(obj="将要进行转换的对象",file="文件名")     将转换的obj写入file，file为必要参数，所以dump只适用于文件操作
f = open("db.txt", "wb")  # 打开文件时要用"字节"方式打开
pickle.dump(d, f)
f.close()

# pickle.loads(转换的字节)     将指定的字节转换成原格式
# 直接转换
d = b'\x80\x03}q\x00(K\x01X\x02\x00\x00\x0011q\x01K\x02X\x02\x00\x00\x0022q\x02u.'
a = pickle.loads(d)
print(a)  # {1: '11', 2: '22'}
# 文件操作
f = open("db.txt", "rb")  # 打开文件时要用"字节"方式打开
a = pickle.loads(f.read())

# pickle.load(file="文件名")     将文件转换成原数据对象，因为file为必要参数，所以load只适用于文件操作
f = open("db.txt", "rb")  # 打开文件时要用"字节"方式打开
d = pickle.load(f)
print(d)  # {1: '11', 2: '22'}


# json.dumps(转换的对象)     将指定的对象转换成字符串
# 直接转换
d = {1: "11", 2: "22"}
a = json.dumps(d)
print(a)  # {"1": "11", "2": "22"}
# 文件操作
f = open("db.txt", "w")  # 打开文件时要用"非字节"方式打开
f.write(json.dumps(d))
f.close()

# json.dump(obj="将要进行转换的对象",fp="文件名")     将转换的obj写入fp，fp为必要参数，所以dump只适用于文件操作
f = open("db.txt", "w")  # 打开文件时要用"非字节"方式打开
json.dump(d, f)
f.close()

# json.loads(转换的内容)     将指定的字符串转换成原格式,因为json的对象必须是str所以 不做之间转换，只能进行文件操作
f = open("db.txt", "r")  # 打开文件时要用"非字节"方式打开
a = json.loads(f.read())
print(a)  # {'1': '11', '2': '22'}
# pickle.load(file="文件名")     将文件转换成原数据对象，因为file为必要参数，所以load只适用于文件操作
f = open("db.txt", "r")  # 打开文件时要用"字节"方式打开
d = json.load(f)
print(d)  # {1: '11', 2: '22'}
