# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 登录系统：需要实现注册，登录，删除，修改密码，管理员对用户解锁
"""
# 用户格式：
f = {
    '身份证号码1': ['姓名', '密码', '输入次数', '是否锁定', '学生', '年龄', '资产', '选课'],
    '身份证号码2': ['姓名', '密码', '输入次数', '是否锁定', '老师', '年龄', '资产', '选课']
}

# 课程格式
cos_list = ['c1', 'c2']
c1 = ['课程名', '上课老师id', ‘教师姓名', '上课时间', '上课教室', '课程费用', '课程种类']
"""


class Detection:  # 验证
    def __init__(self, username, old_f):
        self.user = username
        self.f = old_f

    def test_user(self):
        """
        检测用户是否存在
        :return: true = 存在， false = 不存在
        """
        if self.user in self.f:  # 判断用户是否存在
            return True

    def information(self):
        """
        检测用户登记信息是否正确（输入次数，是否锁定，年龄，用户类别，资产是否只包含数字）
        :return:
        """
        for i in self.f:
            print(i)
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if k == self.user:
                for i in v[2:]:
                    if i.isdigit():  # 判断是否值包含数字
                        return True
                    else:
                        return False

    def test_lock(self):
        """
        检测用户用户是否被锁
        :return: true = 用户未锁， false = 用户已锁
        """
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if k == self.user and int(v[2]) == 0:  # 判断用户是否被锁
                return True
        return False

    def tset_num(self):
        """
        检测用户用户输入次数,输入超过三次将用户锁定
        :return: true = 用户未锁， false = 用户已锁
        """
        # 检测用户是否被锁
        for k in self.f:  # 循环原文件
            v = self.f[k]
            num = int(v[1])  # 将判断锁定的字符串转换为数字
            if k == self.user and 0 <= num < 3:  # 判断用户输入次数是否超限
                return True
            else:
                return False

    def test_courses(self, course):
        """
        判断课程是否已经被用户选择
        :param course: 选择的课程
        :return: False 课程已存在，需要重新选课
        """
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if k == self.user:  # 判断用户名是否正确
                if course in v[7]:  # 判断将要选择的课程是否存在
                    return False
                else:
                    return True


class Login(Detection):  # 登录
    def __init__(self, userID, password, old_f, assets=0):
        self.user = userID  # 身份证号码   key
        self.pwd = password  # 密码  v[1]
        self.f = old_f  # 原文件
        self.ass = assets  # 资产  v[6]

    def register(self, username, species=1, age=None, courses=list()):
        """
        用户注册
        :param username: 用户名（姓名) v[0]
        :param species: 用户种类  v[4]  0表示管路员，1表示学生，2表示老师
        :param age: 年龄  v[5]
        :param courses: 已选课程：默认为空列表  v[7]
        :return: 返回文件列表
        """
        new_user = {self.user: [username, self.pwd, "0", "0", species, age, self.ass, courses]}  # 新的学生用户
        self.f.update(new_user)  # 将新的用户追加到文件：login.txt
        return self.f  # 追加成功

    def login(self):
        """
        用户登录
        :return: True：登录，False：返回
        """
        new_f = {}  # 新的文件

        for k in self.f:  # 循环原文件
            v = self.f[k]
            if self.user == k and self.pwd == v[0]:  # 判断用户名和密码是否正确
                new_v = [v[0], v[1], "0", "0", v[4], v[5], v[6], v[7]]  # 将用户输入次数归零，锁定归零
                new_f.update({k: new_v})  # 将用户追加到新文件
            else:
                new_f.update({k: v})  # 将用户追加到新文件

        return new_f  # 返回新文件

    def delete(self):
        """
         删除用户,仅限管理员使用
        :return:返回新文件列表
        """
        if self.user in self.f.items:
            del self.f[self.user]  # 删除用户

            return self.f  # 返回文件
        return False  # 删除失败

    def change_password(self, new_pwd):
        """
        更改密码
        :return:返回新的文件（字典）
        """
        new_f = {}  # 新文件
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if self.user == k:  # 判断ID是否正确
                new_v = [v[0], new_pwd, v[2], v[3], v[4], v[5], v[6], v[7]]  # 修改用户密码
                new_f.update({k, new_v})  # 将用户追加到新文件
            else:
                new_f.update({k, v})  # 将用户追加到新文件

        return new_f

    def change_num(self):
        """
        更改用户输入次数
        :return: 返回新字典
        """
        new_f = {}
        for k in self.f:  # 循环原文件
            v = self.f[k]
            # 判断用户名是否正确
            if self.user == k:
                # 更改当前用户输入次数并追加到新列表
                new_v = [v[0], v[1], str(int(v[1]) + 1), v[3], v[4], v[5], v[6], v[7]]
                new_f.update({k, new_v})
            else:
                # 对当前记录不做任何更改并追加到新的字典
                new_f.update({k, v})

        return new_f

    def lock(self):
        """
        锁定用户
        :return: 返回新字典
        """
        new_f = {}
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if self.user == k:
                # 将当前用户锁定并添加到新的文件
                new_v = [v[0], v[1], v[2], '1', v[4], v[5], v[6], v[7]]
                new_f.update({k, new_v})

            else:
                # 将当前用户添加到新的文件
                new_f.update({k, v})

        return new_f

    def unlocked(self):

        """
        给用户解锁，仅限管理员使用此功能
        :return: 返回新列表
        """
        new_f = {}
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if self.user == k:
                if v[3] == 1:
                    new_v = [v[0], v[1], v[2], '0', v[4], v[5], v[6], v[7]]
                    new_f.update({k, new_v})
                else:
                    return False
            else:
                new_f.update({k, v})

        return new_f

    def withdraw(self):
        """
        资产提现
        :return:
        """
        # 资产提现
        new_f = dict()  # 新的文件
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if k == self.user:  # 判断用户
                new_ass = int(v[6]) - self.ass  # 提现
                if new_ass >= 0:  # 判断提现后的金额是否大于等于0
                    new_v = [v[0:5], new_ass, v[7]]  # 获取k对应的新的值
                    new_f.update({k: new_v})  # 将新的键值对添加到新文件
                else:
                    return '余额不足，不能提现！'
            else:
                new_f.update({k: v})
        return new_f

    def payment(self):
        """
        缴费，充值，增加资产
        :return:
        """
        new_f = dict()  # 新的文件
        for k in self.f:  # 循环原文件
            v = self.f[k]
            if k == self.user:  # 判断用户
                new_ass = int(v[6]) + self.ass  # 缴费
                if new_ass > int(v[6]):  # 判断缴费后的金额是否大于缴费前的金额
                    new_v = [v[0], v[1], v[2], v[3], v[4], v[5], new_ass, v[7]]  # 获取k对应的新的值
                    new_f.update({k: new_v})  # 将新的键值对添加到新文件
                else:
                    return '缴费未成功！'
            else:
                new_f.update({k: v})
        return new_f


class Course(Login):
    def __init__(self, courses_file):
        self.cos = courses_file  # 课程文件

    def schedule(self, course):
        """
        排课,新增课程
        :param course: 准备要新增的课程
        :return:
        """
        if course in self.cos:  # 判断课程是否存在
            return '课程已存在！请重新排课！'
        else:  # 不存在
            self.cos.append(course)  # 新增课程
            return self.cos  # 返回

    def search(self, condition, position):
        """
        搜索，查找
        :param condition: 搜索条件
        :param position: 搜索条件所在的位置
        :return:
        """
        new_f = []
        for k, i in enumerate(self.cos):
            if i[position] == condition():
                new_f.append(i)  # 将符合时间条件的课程记录添加到新列表
            else:
                continue
            if len(new_f) > 0:
                return new_f
            else:
                return '未找到符合条件的课程！'

    def del_course(self, course):
        """
        删除指定课程
        :param course: 准备要删除的课程
        :return: 返回新的课程列表
        """
        location = self.cos.index(course)  # 要删除的课程的位置
        del self.cos[location]  # 删除指定课程
        return self.cos  # 返回课程列表

        # 用删除和新增实现更改
