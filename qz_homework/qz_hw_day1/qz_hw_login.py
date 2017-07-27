# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 6、用户登陆（三次机会重试）

usr = "renhang"  # 用户名
psw = "000"  # 密码
i = 0  # 初始循环计数
while i < 3:  # 开始循环，循环计数小于3
    username = input("USERNAME:")  # 输入用户名
    passsword = input("PASSWORD:")  # 输入密码
    if usr == username and psw == passsword:  # 用户名和密码正确
        print("welcome!")  # 输出"welcome"
        i = 0  # 返回初始循环计数
        break  # 退出循环
    else:  # 用户名或密码不正确
        print("you are wrong,try again.")  # 输出"you are wrong,try again."
        i += 1  # 循环次数加1





"""
counter = 0
flag = True
while flag:
    username = input("USERNAME:")
    passsword = input("PASSWORD:")
    if counter == 3:
        print("用户被锁定")
        break
    if usr == username and psw == passsword:
        print("welcome!")
        counter = 0
        break
    else:
        print("you are wrong,try again.")
        counter += 1
"""

"""
    if counter < 2:
        if usr == username and psw == passsword:
            print("welcome!")
            counter = 0
            break
        else:
            print("you are wrong,try again.")
            counter += 1
    else:
        if usr == username and psw == passsword:
            print("welcome!")
            counter = 0
            break
        else:
            print("用户被锁定")
            # flag = False
            break
"""



    # if i < 2:
    #     if usr == username and psw == passsword:
    #         print("Welcome!")
    #         break
    #     else:
    #         print("You are wrong!Please try again!")
    #         i += 1
    # else:
    #     if usr == username and psw == passsword:
    #         print("Welcome!")
    #         break
    #     else:
    #         print("sorry!")
    #         break
    #
