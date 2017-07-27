# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 7、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

def func(**kwargs):
    new_dic = {}
    for k, v in kwargs.items():
        l = len(v)
        if l > 2:
            v = v[0:2]
            t = {k: v}
            new_dic.update(t)
        else:
            t = {k: v}
            new_dic.update(t)

    return new_dic


dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}

r = func(**dic)
print("dic:", r)



