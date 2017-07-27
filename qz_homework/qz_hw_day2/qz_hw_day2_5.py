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

exit_flag = True
while exit_flag:
    print("WELCOME".center(40, "-"))
    for k1, v1 in enumerate(dic):  # 循环字典并添加编号
        print(k1, v1)  # 输出省市(一级菜单)
    print("END".center(40, "-"))

    ss_num = input("\n[输入[q]退出] 请输入省市编号:\n")
    if ss_num.isdigit():  # 判断输入的字符串编号是否为数字
        ss_num = int(ss_num)  # 转换成数字
        if 0 < ss_num < len(dic):  # 判断输入的编号是否存在
            p = dic[v1]  # 取出编号对应的字典(二级菜单)
            for i in range(3):
                print(" WELCOME TO [%s] ".center(40, "-") % v1)
                for k2, v2 in enumerate(p):  # 循环二级菜单并添加编号
                    print(k2, v2)  # 输出二级菜单
                print("END".center(40, "-"))

                xq_num = input("\n[输入[q]退出],输入[b]返回顶级菜单并重新输入] 请输入县区编号:\n")
                if xq_num.isdigit():  # 判断输入的字符串编号是否为数字
                    xq_num = int(xq_num)  # 转换成数字
                    if 0 < xq_num < len(v1):  # 判断输入的编号是否存在
                        c = dic[v1][v2]  # 取出编号对应的列表(三级菜单)

                        print(" WELCOME TO [%s] ".center(40, "-") % v2)
                        for k3, v3 in enumerate(c):  # 循环三级菜单并添加编号
                            print(k3, v3)  # 输出三级菜单
                        print("END".center(40, "-"))
                        q_b = input("\n[输入[q]退出],输入[b]返回顶级菜单并重新输入] :\n")
                        if q_b == "q":  # 输入q退出
                            print("BYE!")
                            continue
                        elif q_b == "b":  # 输入b返回上级菜单
                            continue
                        else:
                            print("输入错误!退出!")
                            break
                    else:
                        print("您输入的编号不存在,请重新输入:\n")
                        continue
                elif xq_num == "q":  # 输入q退出
                    print("BYE!")
                    exit_flag = False
                elif xq_num == "b":  # 输入b返回上级菜单
                    break
        else:
            print("您输入的编号不存在,请重新输入:\n")
            continue
    elif ss_num == "q":  # 输入q退出
        print("BYE!")
        exit_flag = False



