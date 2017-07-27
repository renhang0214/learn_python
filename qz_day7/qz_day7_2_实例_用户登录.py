# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 实例 ==>> 用户登录：
# strip()   使用strip时无参数默认去掉两端的空格和换行符\n，有参数则去掉两端的指定值（即参数值）
# split()   用参数分割字符串（"alex|123" ==>> split("|") ==>> "alex","123")



# 方法1
"""
user = input("USERNAME:")
pwd = input("PASSWORD:")
f = open("db.txt", 'r', encoding="utf-8")
for line in f:
    line = line.strip()
    line_list = line.split("|")
    print(line_list)
    if user == line_list[0] and pwd == line_list[1]:
      print("登录成功！")
      break
"""

# 方法2
def login(username, password):
    """
    用于用户名密码验证
    :param username:用户名
    :param password:密码
    :return:True：验证成功；False：验证失败
    """
    f = open("db.txt", 'r', encoding="utf-8")
    for line in f:
        line = line.strip()
        line_list = line.split("|")
        if user == line_list[0] and pwd == line_list[1]:
            return True
        return False
user = input("USERNAME:")
pwd = input("PASSWORD:")
# is_login = login(user, pwd)
# if is_login:
if login(user, pwd):
    print("登录成功")
else:
    print("失败")
