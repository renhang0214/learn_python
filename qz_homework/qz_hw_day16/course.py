# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import pickle
import getpass

from lib import UserLogin as lg


def main(arg):
    while True:  # 开始死循环
        print('\033[1;34m%s\033[0m' % arg)

        print(" WELCOME ".center(40, "*"), "\n")
        a = input("【1】注册【2】登录【3】退出\n\n请输入对应的编号：\n")  # 用户输入  删除用户【4】给用户解锁【5】修改密码【6】
        if a.isdigit():
            if a == '1':
                for i in range(3):
                    user = input("身份证号码：")
                    if len(user) != 18:
                        print('身份证号码输入错误！\033[1;31m 请输入 18 位身份证号码！ \033[0m')
                        continue
                    name = input('姓名：')
                    pwd = getpass.getpass("密码：")
                    age = input('年龄：')

                    ret = lg.Login(user, pwd, arg)  # 传入参数

                    if ret.test_user():  # 判断用户是否存在
                        print('\n\033[1;31m 用户【 %s 】已被注册已，请重新输入！ \033[0m\n')
                    else:
                        new_f = ret.register(name, age=age)
                        # 将新的文件写入（打开文件时要用"字节"方式打开）
                        pickle.dump(new_f, open("login.txt", "wb"))
                        f.close()

                        break

            elif a == '2':
                for i in range(3):
                    user = input("身份证号码：")
                    if len(user) != 18:
                        print('身份证号码输入错误！\033[1;31m 请输入 18 位身份证号码！ \033[0m')
                        continue
                    pwd = getpass.getpass("密码：")

                    ret = lg.Login(user, pwd, arg)

                    if ret.test_user:  # 判断用户是否存在
                        if ret.information:  # 判断用户登记信息是否正确
                            if ret.test_lock:  # 判断用户是否被锁
                                if ret.tset_num:  # 判断用户输入次数是否超过3次
                                    new_f = ret.login()
                                    # 将新的文件写入（打开文件时要用"字节"方式打开）
                                    pickle.dump(new_f, open("login.txt", "wb"))
                                    f.close()

                                    ladn(user)




                                else:
                                    print('\033[1;31m输入错误次数超限，用户已被锁定，请联系管理员解锁！\033[0m')
                                    new_f = ret.lock()
                                    pickle.dump(new_f, open('login.txt', 'wb'))
                                    f.close()
                            else:
                                print('\033[1;31m输入错误次数超限，用户已被锁定，请联系管理员解锁！\033[0m')
                        else:
                            print('提示：\033[1;31m用户信息登记错误，请联系管理员！v\033[0m')
                    else:
                        print('用户【 %s 】不存在,请重新输入：\n" % user')
                        pass
            else:
                print('\n\033[1;31m 输入错误！ \033[0m\n')

        else:
            print('\n\033[1;31m 输入错误！ \033[0m\n')
            print('\033[1;31m用户信息登记错误，请联系管理员！'
                  '错误提示：v\033[0m')
            #     # elif a == 3:  # 用户输入3：删除
            #     #     for i in range(3):
            #     #         print("---------".center(40, "-"))
            #     #         username = input("请输入管理员账户：")
            #     #         password = input("请输入密码：")
            #     #         if username == "admin" and password == "123456":
            #     #             user = input("请输入要删除的用户：")
            #     #
            #     #             if test(user):  # 判断用户是否存在
            #     #                 delete(user)  # 执行delete函数
            #     #                 continue
            #     #             else:
            #     #                 print("用户【 %s 】不存在,请重新输入：\n" % user)
            #     #                 continue  # 重新开始第二层循环
            #
            #     elif a == 4:  # 用户输入4
            #         exit(" GOODBYE ".center(40, "*"))  # 退出死循环
            #     else:
            #         print("\n""您输入编号的不存在，请重新输入:\n")
            #         continue  # 重新开始死循环
            # else:
            #     print("\n""请输入对应的编号：\n")
            #     continue  # 重新开始死循环


def ladn(arg):
    f = open('login.txt', 'rb')
    old_f = pickle.load(f)  # 得到的文件列表为字典
    f.close()

    print("【%s】欢迎登陆".center(40, "-") % arg)
    name = old_f[arg][0]
    species, age, assets, course = old_f[arg][4:]

    print('ID：%s，姓名：%s，种类：%s，年龄：%s，账户余额：%s，已学课程：'
          % (arg, name, species, age, assets))  # 输出用户信息
    if assets == []:
        print('\033[1;32m您还未进行学习！\033[0m')
    else:
        for k, i in enumerate(assets, 1):
            print(k, i)
    if assets == '0':  # 管理员
        # 增加教师用户
        # 删除用户
        # 查找用户
        # 为用户重置
        # 排课，增加新课程并为教师增加资产
        # 更改课程
        # 删除课程
        # 查找课程

        pass
    elif assets == '2':  # 教师
        # 资产提现
        # 修改密码
        #
        pass
    elif assets == '1':  # 学生
        # 充值
        # 选课
        # 修改密码
        # 查找课程
        pass
    else:
        pass


if __name__ == '__main__':

    try:
        f = open('login.txt', 'rb')
        old_f = pickle.load(f)  # 得到的文件列表为字典
        f.close()
    except Exception as e:

        print('\n')
        print('\033[1;31m还未有用户注册，请联系管理员或注册！\033[0m')
        print('\n')
        old_f = {}
    finally:
        main(old_f)
