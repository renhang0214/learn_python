# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数

def fun(s):
    con_sa = 0
    con_int = 0
    con_sp = 0
    con_other = 0
    for i in s:
        if i.isdigit():
            con_int += 1
        elif i.isalpha():
            con_sa += 1
        elif i.isspace():
            con_sp += 1
        else:
            con_other += 1
    print("数字：%s 个，字母：%s 个，空格：%s 个，其他：%s 个" %(con_sa, con_int, con_sp, con_other))

    return

fun("ajfuy6r1928smbdfa(%#@")


