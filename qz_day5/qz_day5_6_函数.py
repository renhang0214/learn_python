# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# 函数
# 实例：发送邮件
"""
def Email():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    msg = MIMEText('邮件内容', 'plain', 'utf-8')
    msg['From'] = formataddr(["武沛齐", 'wptawy@126.com'])
    msg['To'] = formataddr(["走人", '297096995@qq.com'])
    msg['Subject'] = "主题"

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("wptawy@126.com", "WW.3945.59")
    server.sendmail('wptawy@126.com', ['297096995@qq.com', ], msg.as_string())
    server.quit()

Email()
"""

# def 函数名（参数）：  函数名不能是中文
#     函数体
#     return 值  只要执行return，return下面的代码将不再执行

'''
默认参数：（放在参数最后）
    def xxx(a):
        aaa = a + "ooo"
        print(aaa)
        return aaa
    xxx("1")    ==>> 1ooo

    def xxx(a="b"):
        aaa = a + "ooo"
        print(aaa)
        return aaa
    xxx()       ==>> booo
'''

'''
动态参数：
    def xxx(*args)：
        return aaa
    xxx(11，22) ==>>(元组）

    def xxx(**kwargs)：
        return aaa
    xxx(“k1”=11，”k2”=22) ==>>（字典）

    def xxx(*args，**kwargs)： ==>>万能参数
        return aaa
    xxx(11，22，“k1”=11，”k2”=22) ==>> (元组，字典）
'''

'''
全局变量、局部变量
    全局变量：所有人都能用（书写规范：大写）
    局部变量：一个人可以用（书写规范：小写）

p = "alex"  # 全局变量

def fun1():
    a = 123
    global p  # 指定p为全局变量
    p = "eric"  # 局部变量
    print(a)  # ==>> 123

fun1()

def fun2():
    a = 456
    print(p)  # ==>> alex  指定p后==>> eric
    print(a)  # ==>> 456

fun2()
'''





