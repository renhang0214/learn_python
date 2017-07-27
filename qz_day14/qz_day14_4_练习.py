# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


"""
会员信息
会员A: 会员号:HY0001,积分：3
会员B: 会员号：HY0002,积分：5
会员C: 会员号：HY0003,积分：10

购买一次商品 + 1 分，退一次商品 - 1 分
"""


class Member:
    """Name：姓名, MemberNo：会员号, Integral：积分"""

    def __init__(self, Name, MemberNo, Integral):
        self.name = Name
        self.no = MemberNo
        self.integral = Integral

    def buy(self):
        """注释：购买商品"""

        self.integral = self.integral + 1

    def retreat(self):
        """注释：退货"""

        self.integral = self.integral - 1

    def detail(self):
        """注释：会员的详细信息"""

        temp = "姓名:%s ; 会员号:%s ; 积分:%s" % (self.name, self.no, self.integral)
        print(temp)


# 员工信息
HYA = Member('Aa', "HY0001", 3)  # 创建苍井井角色
HYB = Member('B', "HY0002", 5)  # 创建东尼木木角色
HYC = Member('C', "HY0003", 10)  # 创建波多多角色
# 输出原始信息
print("原始信息".center(30, "-"))
HYA.detail()
HYB.detail()
HYC.detail()
# 开始记录
print("第一次记录".center(30, "-"))
HYA.buy()  # 会员A买了一次
HYB.retreat()  # 会员B退了一次
HYC.buy()  # 会员C买了一次

# 输出当前所有人的详细情况
HYA.detail()
HYB.detail()
HYC.detail()

print("第二次记录".center(30, "-"))
HYA.buy()  # 会员A买了一次
HYB.buy()  # 会员B买了一次
HYC.retreat()  # 会员C退了一次

# 输出当前所有会员的详细信息
HYA.detail()
HYB.detail()
HYC.detail()
