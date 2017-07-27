# /user/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

import re  # 调用re模块

# 原字符串
a = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2**5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"


# 因为计算的值可能会有小数，所以在进行字符串与数字转换的时候全部用flost（浮点）转换
def addition_subtraction(args):  # addition加法，subtraction减法
    """
    对表达式进行加法或者减法
    :param args: 需要计算表达式
    :return: addition_subtraction(arg)：递归；args：需要计算表达式
    """
    if "+-" or "++" or "-+" or "--" in args:  # 判断表达式内是否包含"+-" or "++" or "-+" or "--" 符号
        args = re.sub("\+\-", "-", args)
        args = re.sub("\+\+", "+", args)
        args = re.sub("\-\-", "+", args)
        args = re.sub("\-\+", "-", args)
    # ride_value：需要进行加减匹配的值
    ride_value = re.split("(\d+\.?\d*\s*[+-]\s*\d+\.?\d*)", args, maxsplit=1)  # 匹配乘除
    if len(ride_value) == 3:  # 判断匹配结果长度是否为3

        v1, v2, v3 = ride_value  # v1:匹配值得第一位；v2:匹配值得第二位；v3:匹配值的第三位

        if "+" in v2:  # 判断是否有加法
            result = re.split("\+", v2)  # 匹配将要相加的值
            if re.search("^\-", args):  # 判断初始被匹配的表达式是否为负数
                v2 = float(result[0]) - float(result[1])  # 计算v2的值
            else:
                v2 = float(result[0]) + float(result[1])  # 计算v2的值
        elif "-" in v2:  # 判断是否有减法
            result = re.split("\-", v2)  # 匹配将要想减的值
            if re.search("^\-", args):  # 判断初始被匹配的表达式是否为负数
                v2 = float(result[0]) + float(result[1])  # 计算v2的值
            else:
                v2 = float(result[0]) - float(result[1])  # 计算v2的值
        arg = v1 + str(v2) + v3  # 得到新的表达式
        return addition_subtraction(arg)  # 返回加减函数（递归）
    else:
        return args  # 返回初始需要进行计算的表达式


def ride_except(args):  # ride乘，except除
    """
    对表达式进行乘法或者除法的运算
    :param args:需要计算表达式
    :return:args：需要计算表达式；ride_except(arg)递归
    """
    # ride_value：需要进行乘除匹配的值
    ride_value = re.split("(\d+\.?\d*"  # 整数或者浮点数
                          "([*/]|\*\*)"  # 匹配×或÷
                          "[+-]*\d+\.?\d*)",  # 整数或者浮点数
                          args,
                          maxsplit=1,
                          flags=re.X)
    if len(ride_value) == 4:  # 判断匹配结果长度是否为3
        # v1:匹配值得第一位；v2:匹配值得第二位；v3:匹配值的第三位（无任何意义忽略）;v4:匹配值的第四位
        v1, v2, v3, v4 = ride_value

        if "**" in v2:  # 判断是否有乘法
            result = re.split("\*\*", v2)  # 匹配将要相乘的值
            v2 = float(result[0]) ** float(result[1])  # 计算v2的值
        elif "*" in v2:
            result = re.split("\*", v2)  # 匹配将要相乘的值
            v2 = float(result[0]) * float(result[1])  # 计算v2的值
            pass
        elif "/" in v2:  # 判断是否有除法
            result = re.split("\/", v2)  # 匹配将要相除的值
            v2 = float(result[0]) / float(result[1])  # 计算v2的值
        arg = v1 + str(v2) + v4  # 得到新的表达式
        return ride_except(arg)  # 返回乘除函数（递归）
    else:
        return args  # 返回初始需要计算的表达式


def main(a):  # 主函数
    """
    对表达式进行运算
    :param arg: 需要计算的表达式
    :return: main(new_arg)：递归；
    """
    arg = str()  # 建一个新的字符串
    for i in a:  # 循环表达式a
        if i == " ":  # 判断是否为空格
            pass  # 不做任何操作
        else:
            arg += i  # 新字符串等于原字符串加

    result = re.split("\(([^()]+)\)", arg, maxsplit=1)  # 取括号内的表达式

    if len(result) == 3:  # 判断取出的值长度是否为3
        before, arg_sum, after = result  # before:匹配值得第一位；arg_sum:匹配值得第二位；after:匹配值的第三位
        # 我们需要的表达式为第二位
        new_result = addition_subtraction(ride_except(arg_sum))  # 先执行乘除函数再执行加减函数
        new_arg = before + new_result + after  # 得到新的表达式
        return main(new_arg)  # 范湖函数值

    else:
        a = str(a)  # 将表达式a转换成str
        new_result = addition_subtraction(ride_except(a))  # 先执行乘除函数再执行加减函数
        return new_result  # 返回函数值


result = main(a)

print("\n", "计算器得到的计算结果".center(40, "*"),
      "\n\n", result.center(40))

# 原字符串的表达式
arg_result = 1 - 2 * (
    (60 - 30 + (-40.0 / 5) * (9 - 2 ** 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (16 - 3 * 2))
print("\n", "应得的计算结果".center(40, "*"),
      "\n\n", str(arg_result).center(40))
