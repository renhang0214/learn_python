# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

import pickle

f = open('login.txt', 'rb')
old_f = pickle.load(f)  # 得到的文件列表为字典
f.close()

print(old_f)

class Login:  # 登录
    def __init__(self, userID, password, old_f, assets=0):
        self.user = userID  # 身份证号码   key
        self.pwd = password  # 密码  v[1]
        self.f = old_f  # 原文件
        self.ass = assets  # 资产  v[6]

    def login(self):
        """
        用户登录
        :return: True：登录，False：返回
        """
        new_f = {}  # 新的文件
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if self.user == k and self.pwd == v[0]:  # 判断用户名和密码是否正确
                new_v = [v[0],v[1], "0", "0", v[4],v[5],v[6],v[7]]  # 将用户输入次数归零，锁定归零
                new_f.update({k: new_v})  # 将用户追加到新文件
            else:
                new_f.update({k: v})  # 将用户追加到新文件

        return new_f  # 返回新文件

ret = Login('111111111111111111', '1', old_f=old_f,).login()
print(ret)