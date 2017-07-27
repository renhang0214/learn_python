# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 面向对象 ==>> 进阶5
# 特殊方法

# __call__
class F:
    def __init__(self):
        print('init')
        self.n = 'n'
        xx = 'xx'

    def __call__(self, *args, **kwargs):  # *args, **kwargs 万能参数
        print('call')
        return args, kwargs

    def __getitem__(self, item):  # 获取 在2.7版本中是getlice
        print(item)

    def __setitem__(self, key, value):  # 赋值
        print(key, value)

    def __iter__(self):  # 执行for循环是自动执行
        yield 1
        yield 2
        yield 3

    def __delitem__(self, key):  # 删除
        print(key)

    def __str__(self):
        return 'str方法'

r = F()()  # 自动执行init与call
print(r)  # 拿到call的返回值args, kwargs
r = F()
r['k1']  # 自动执行getitem（在2.7版本中是getlice）并将k1传给item
r['k1'] = [11, 123]  # 自动执行setitem并给key, value赋值，
print(1, F().__dict__)  # F()为类的对象，F().__dict__获取对象的所有成员
print(2, F.__dict__)  # 获取类的所有成员（字段）
for i in r:  # 自动执行iter
    print('iter', i)
del r['k1']  # 自动执行delitem并删除key

print(F())  # 自动执行init与str方法，并返回return值
