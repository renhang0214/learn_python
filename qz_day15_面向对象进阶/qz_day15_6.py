# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶6
# 异常（错误）处理

"""
异常（错误）语法1
try:
    pass
except 异常类的名称 as 对象名:  # 对象名是为异常类创建的对象
    pass
"""

"""
异常（错误）语法2
try:
    pass
except Exception as e:  # 异常可以写多个，按顺序执行
    # 异常时进行的操作
    pass
else:
    # 无异常时进行的操作
    pass
finally:
    无论是否异常最后都要进行的操作
    pass
"""
a = input('请输入:')
try:
    if a == 'a':
        print('123')
    else:
        raise Exception('出错了')  # 主动触发错误
except Exception as e:  # 封装错误信息的对象
    print(e)


#断言：不成立则把报错<多用于测试>
assert 1 == 2
