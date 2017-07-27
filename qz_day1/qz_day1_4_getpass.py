# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

import getpass  # 导入getpass模块,用于输入密码不可见

user = input("username:")
paw = input("password:")
paw2 = getpass.getpass("password2:")  # 输入时不可见
print(user)
print(paw)

"""
打印结果:(用户输入的内容)
    renhang
    123
    123
"""