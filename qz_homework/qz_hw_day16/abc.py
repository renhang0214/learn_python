# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang
import pickle

f = open('login.txt', 'rb')
old_f = pickle.load(f)  # 得到的文件列表为字典
f.close()
print(old_f)

species, age, assets, course = old_f['111111111111111111'][4:]

print(species,age,assets)