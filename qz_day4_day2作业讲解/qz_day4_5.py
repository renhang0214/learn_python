# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author:Ren Hang


"""
五、用户交互，显示省市县三级联动的选择
"""

dic = {
    "北京": {
        "朝阳区": ["123", "456"],
        "崇文区": ["789", "101"]
    },
    "辽宁省": {
        "沈阳市": ["铁西区", "沈河区"],
        "锦州市": ["古塔区", "黑山县"],
    },
}
# 方法1
# 循环输出所以的省
for x in dic:
    print(x)

i1 = input("请输入省份：")
a = dic[i1]

# 循环输出所以的市
for j in a:
    print(j)

i2 = input("请输入市：")
b = dic[i1][i2]

for z in b:
    print(z)
