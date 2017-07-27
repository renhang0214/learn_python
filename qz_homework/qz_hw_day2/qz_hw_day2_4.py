# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

"""
购物车
功能要求：
1.要求用户输入总资产，例如：2000
2.显示商品列表，让用户根据序号选择商品，加入购物车
3.购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
4.附加：可充值、某商品移除购物车
"""

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
shop_car = []

wage = input("请输入工资:")  # 输入工资
if wage.isdigit():  # 判断输入字符串是否只含数字
    wage = int(wage)  # 转换成数字
else:  # 不是只有数字
    exit("你输入的不是数字!")  # 报错

exit_flag = False  # 设置标记

while not exit_flag:

    print("Welcome".center(33, "*"))  # 欢迎
    print("商品列表".center(30, "-"))  # 商品列表
    for k, i in enumerate(goods):  # 循环商品并添加序号
        name = i["name"]  # 取商品名
        money = i["price"]  # 取商品价格
        print(k, name, money)  # 输出商品列表
    print("".center(33, "-"))

    print("\n您共有资产 [%s] 元钱." % wage)
    shop_num = input("[输入[q]退出,输入[d]删除购物车内其他商品] 请输入要购买的商品编号:\n")

    if shop_num.isdigit():  # 判断是否购买,输入数字为购买
        shop = int(shop_num)  # 字符串转换成数字
        if shop < len(goods):  # 判断输入的序号是否在商品列表
            s_item = goods[shop]  # 调出所选商品
            if s_item["price"] <= wage:  # 商品价格与工资做对比
                shop_car.append(s_item)   # 放入购物车
                # shop_car["counter"] += 1
                wage -= s_item["price"]  # 余额
                print("\n您已经购买了 [%s],您还有 [%s] 元钱。\n" % (s_item["name"], wage))
                print("已购商品".center(30, "-"))  # 已购商品
                # print(shop_car)
                for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
                    s_name = s_i["name"]  # 取出商品名称
                    s_money = s_i["price"]  # 取出商品金额
                    print(s_k, s_name, s_money)  # 输出已购买商品列表
                print("".center(33, "-"))
            else:
                print("已购商品".center(30, "-"))  # 已购商品
                # print(shop_car)
                for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
                    s_name = s_i["name"]  # 取出商品名称
                    s_money = s_i["price"]  # 取出商品金额
                    print(s_k, s_name, s_money)  # 输出已购买商品列表
                print("".center(33, "-"))
                recharge = input("\n[输入[q]退出,输入[d]删除购物车内其他商品] 您的余额不足,请输充值:\n")
                if recharge.isdigit():  # 数字
                    recharge = int(recharge)
                    wage += recharge
                elif recharge == "q":  # 退出
                    print("再见!")
                    exit_flag = True
                    # break
                elif recharge == "d":  # 删除
                    for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
                        s_name = s_i["name"]  # 取出商品名称
                        s_money = s_i["price"]  # 取出商品价格
                    del_shop = int(input("请输入要删除的商品编号:"))
                    if del_shop.isdigit():
                        if int(del_shop) < len(shop_car):

                            del_shop = int(del_shop)
                            del_money = shop_car[del_shop]["price"]
                            wage += del_money
                            del shop_car[del_shop]

                            print("已购商品".center(30, "-"))  # 已购商品
                            # print(shop_car)
                            for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
                                s_name = s_i["name"]  # 取出商品名称
                                s_money = s_i["price"]  # 取出商品金额
                                print(s_k, s_name, s_money)  # 输出已购买商品列表
                            print("".center(33, "-"))
                        else:
                            print("您输入的数字编号不正确!")
                            continue
                    else:
                        print("您输入的商品编号不正确")
                else:
                    continue

        else:
            print("\n您输入的商品不存在!\n")
            continue
    elif shop_num == "q":
        print("再见!")
        exit_flag = True
        # break
    elif shop_num == "d":  # 删除
        for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
            s_name = s_i["name"]  # 取出商品名称
            s_money = s_i["price"]  # 取出商品价格
        del_shop = input("请输入要删除的商品编号:")
        if del_shop.isdigit():
            if int(del_shop) < len(shop_car):

                del_shop = int(del_shop)
                del_money = shop_car[del_shop]["price"]
                wage += del_money
                del shop_car[del_shop]
                print("已购商品".center(30, "-"))  # 已购商品
                # print(shop_car)
                for s_k, s_i in enumerate(shop_car):  # 循环购物车商品并添加序号
                    s_name = s_i["name"]  # 取出商品名称
                    s_money = s_i["price"]  # 取出商品金额
                    print(s_k, s_name, s_money)  # 输出已购买商品列表
                print("".center(33, "-"))
            else:
                print("您输入的数字编号不正确!")
                continue
        else:
            print("您输入的商品编号不正确")
    else:
        continue
