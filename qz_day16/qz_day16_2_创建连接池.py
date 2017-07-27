# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

# 创建连接池
class ConncetionPool:  # ConncetionPoo连接池
    __obj = None  # 创建私有字段，用于判断

    def __init__(self):
        pass

    @staticmethod  # 静态方法
    def get_obj():
        if ConncetionPool.__obj:  # 判断__obj
            return ConncetionPool.__obj  # 返回__obj
        else:
            ConncetionPool.__obj = ConncetionPool()  # 创建对象并赋值给__obj
            return ConncetionPool.__obj  # 返回__obj


pool1 = ConncetionPool.get_obj()  # 执行类的静态方法
print(pool1)
pool2 = ConncetionPool.get_obj()  # 执行类的静态方法
print(pool2)
pool3 = ConncetionPool.get_obj()  # 执行类的静态方法
print(pool3)


# for i in range(10):
#     pool = ConncetionPool.get_obj()  # 执行类的静态方法
#     print('去连接池', pool, '中获取一个连接')
#     conn = pool.get_connection
#     print(conn)
