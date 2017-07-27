# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 内置函数
# __import__（）用于导入模块
# getattr 用于寻找模块的指定对象
# a = __import__(‘b’)  # b为模块名,b是字符串 ==>> 导入模块b并重新命名为a
# c = getattr(a,’d’)  # d为模块中指定对象 ==>> 找到模块中命名为d的对象
# d() ==>> 执行d

# getattr(a,’b’, c)  # 从a模块中导入b。c参数可不写表示找不到报错；c为None表示找不到不报错，返回None。
# hasattr(a,’b’)  # 判断a中b模块是否存在。
# setattr(a,’b’, c)  # 在内存中我模块a创建b=c。
# delattr(a,’b’)  # 在内存中删除模块a中的b。
