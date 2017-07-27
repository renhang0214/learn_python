# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

"""
四、购物车
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
# 方法2
# asset_all 总资产
asset_all = 0
# car_dict 购物车
car_dict = {}
# all_pric 已经购买所以的商品总价
all_price = 0
# all_sum 已经购买单个的商品总价
all_sum = 0

i1 = input("请输入总资产：")
asset_all = int(i1)

for i in goods:
    print(i["name"], i["price"])

while True:
    i2 = input("【Y/y：结算】输入要购买的商品名称：")
    if i2.lower() == "y":
        break
    for item in goods:
        if item["name"] == i2:
            name = item["name"]
            if name in car_dict.keys():
                car_dict[name]["num"] += 1
            else:
                car_dict[name] = {"num": 1, "single_price": item["price"]}
    print(car_dict)

for k, v in car_dict.items():
    all_sum = v["num"] * v["single_price"]
    all_price += all_sum

if all_price > asset_all:
    print("余额不足！")
else:
    print("购买成功！")
