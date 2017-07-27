# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 登录系统：需要实现注册，登录，删除，

def test(username):
    """
    检测用户名是否存在
    :param username: 用户名
    :return: true = 存在， false = 不存在
    """
    with open("login.txt", 'r', encoding="utf-8")as f:  # 以只读模式打开文件：login.txt
        for line in f:  # 按行循环读取文件
            line_list = line.strip().split("|")  # 去掉空格与换行符并用"|"分割
            if username == line_list[0]:  # 判断用户是否存在
                return True
        return False


def test_num(username):
    """
    检测用户用户是否被锁
    :param username: 用户名
    :return: true = 用户未锁， false = 用户已锁
    """
    with open("login.txt", 'r', encoding="utf-8")as f:  # 以只读模式打开文件：login.txt
        for line in f:  # 按行循环读取文件
            line_list = line.strip().split("|")  # 去掉空格与换行符并用"|"分割
            if line_list[0] == username and int(line_list[3]) == 0:  # 判断用户是否被锁
                return True
        return False


def user_num(username):
    """
    检测用户用户输入次数
    :param username: 用户名
    :return: true = 用户未锁， false = 用户已锁
    """
    with open("login.txt", 'r', encoding="utf-8")as f:  # 以只读模式打开文件：login.txt
        for line in f:  # 按行循环读取文件
            line_list = line.strip().split("|")  # 去掉空格与换行符并用"|"分割
            num = int(line_list[1])
            if line_list[0] == username and 0 <= num < 3:  # 判断用户输入次数
                return True
            # else:
            #     f.close()
    with open("login.txt", 'r+', encoding="utf-8")as f:  # 以只读模式打开文件：login.txt
        # 将文件内的用户存入列表
        li = list(f)
        # 清空文件
        f.truncate(0)
        # 新列表
        new_li = []
        # 循环列表li
        for i in li:
            # 去除空格，换行符并用"|"分割
            new_i = i.strip().split("|")
            # 判断用户名和密码是否正确
            if username == new_i[0]:
                # print("删除用户【%s】成功" % username, "\n")
                # 不做任何操作继续循环
                i = new_i[0] + "|" + new_i[1] + "|" + new_i[2] + "|" + "1" + "\n"
                new_li.append(i)
            else:
                # 将用户名密码添加到新列表new_li
                i = new_i[0] + "|" + new_i[1] + "|" + new_i[2] + "|" + new_i[3] + "\n"
                new_li.append(i)

        with open("login.txt", 'a', encoding="utf-8")as f:  # 以追加模式打开文件：login.txt
            # 循环新列表
            for i in new_li:
                # 将新列表的内容转换成字符串并添加到文件
                f.write(str(i))
                # return True  # 删除成功
        return False


def register(username, password):
    """
    用户注册
    :param username: 用户名
    :param password: 密码
    :param num: 计数器
    :return: true = 注册成功， false = 注册失败
    """
    with open("login.txt", 'a', encoding="utf-8")as f:  # 以追加模式打开文件：login.txt
        new_user = username + "|" + "0" + "|" + password + "|" + "0" + "\n"  # 新的用户
        f.write(new_user)  # 将新的用户追加到文件：login.txt
        return True  # 追加成功


def login(username, password):
    """
    验证用户名和密码
    :param username: 用户名
    :param password: 密码
    :return: true = 登录成功， false = 登录失败
    """
    with open("login.txt", 'r+', encoding="utf-8")as f:  # 以读写模式打开文件：login.txt
        # 将文件内的用户存入列表
        li = list(f)
        # 清空文件
        f.truncate(0)
    new_li = []  # 新列表

    # 循环列表li
    for i in li:
        # 去除空格，换行符并用"|"分割
        new_i = i.strip().split("|")
        # 判断用户名和密码是否正确
        if username == new_i[0]:
            if password == new_i[2]:
                print("欢迎登录 ".center(40, "-"), "\n")
                i = new_i[0] + "|" + "0" + "|" + new_i[2] + "|" + "0" + "\n"
                new_li.append(i)
            else:
                print("用户名或密码不正确，请重新输入：\n")
                new_i[1] = int(new_i[1])
                new_i[1] += 1
                new_i[1] = str(new_i[1])
                i = new_i[0] + "|" + new_i[1] + "|" + new_i[2] + "|" + new_i[3] + "\n"
                new_li.append(i)
        else:
            i = new_i[0] + "|" + new_i[1] + "|" + new_i[2] + "|" + new_i[3] + "\n"
            new_li.append(i)
            pass
    with open("login.txt", 'a', encoding="utf-8")as f:  # 以追加模式打开文件：login.txt
        # 循环新列表
        for i in new_li:
            # 将新列表的内容转换成字符串并添加到文件
            f.write(str(i))


def delete(username):
    """
     删除用户
    :param username:用户名
    :return:
    """
    with open("login.txt", 'r+', encoding="utf-8")as f:  # 以读写模式打开文件：login.txt
        # 将文件内的用户存入列表
        li = list(f)
        # 清空文件
        f.truncate(0)

    # 新列表
    new_li = []
    # 循环列表li
    for i in li:
        # 去除空格，换行符并用"|"分割
        new_i = i.strip().split("|")
        # 判断用户名和密码是否正确
        if username == new_i[0]:
            print("删除用户【%s】成功" % username, "\n")
            # 不做任何操作继续循环
            continue
        else:
            # 将用户名密码添加到新列表new_li
            i = new_i[0] + "|" + new_i[1] + "|" + new_i[2] + "|" + new_i[3] + "\n"
            new_li.append(i)

    with open("login.txt", 'a', encoding="utf-8")as f:  # 以追加模式打开文件：login.txt
        # 循环新列表
        for i in new_li:
            # 将新列表的内容转换成字符串并添加到文件
            f.write(str(i))
            # return True  # 删除成功


def main():
    while True:  # 开始死循环
        print(" WELCOME ".center(40, "*"), "\n")
        a = input("【1】注册【2】登录【3】删除用户【4】退出\n\n请输入对应的编号：\n")  # 用户输入

        if a.isdigit():  # 判断用户输入的字符串是否只包含数字
            a = int(a)  # 字符串转换成数字
            if a == 1:  # 用户输入1：注册
                for i in range(3):  # 循环三次
                    print("---------".center(40, "-"))
                    user = input("请输入用户名：")
                    pwd = input("请输入密码：")
                    if test(user):  # 判断用户名是否存在
                        print("用户【 %s 】已注册，请重试!" % user)
                        continue  # 重新开始第二层循环
                    else:
                        register(user, pwd)  # 执行register函数
                        print("注册成功！")
                        break  # 退出第二层循环

            elif a == 2:  # 用户输入2：登录
                # for i in range(3):
                print("---------".center(40, "-"))
                user = input("请输入用户名：")
                pwd = input("请输入密码：")

                if test(user):  # 判断用户名是否存在
                    if test_num(user):  # 判断用户是否被锁定
                        if user_num(user):  # 判断此用户名输入的次数
                            login(user, pwd)  # 执行login函数
                        else:
                            print("用户【 %s 】输入错误过多，已被锁定，请联系管理员解锁！\n" % user)
                            continue
                    else:
                        print("用户【 %s 】被锁定，请联系管理员解锁！\n" % user)
                        continue
                else:
                    print("用户【 %s 】不存在,请重新输入：\n" % user)
                    continue

            elif a == 3:  # 用户输入3：删除
                for i in range(3):
                    print("---------".center(40, "-"))
                    username = input("请输入管理员账户：")
                    password = input("请输入密码：")
                    if username == "admin" and password == "123456":
                        user = input("请输入要删除的用户：")

                        if test(user):  # 判断用户是否存在
                            delete(user)  # 执行delete函数
                            continue
                        else:
                            print("用户【 %s 】不存在,请重新输入：\n" % user)
                            continue  # 重新开始第二层循环

            elif a == 4:  # 用户输入4
                exit(" GOODBYE ".center(40, "*"))  # 退出死循环
            else:
                print("\n""您输入编号的不存在，请重新输入:\n")
                continue  # 重新开始死循环
        else:
            print("\n""请输入对应的编号：\n")
            continue  # 重新开始死循环


main()
