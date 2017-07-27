# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# open函数
"""
打开文件:(两种方式)
    1.f = open("文件名", '打开方式')
    2.with open("文件名", '打开方式', encoding="uttf-8") as f:
        # 'r'只读文件
        # 'w'只写文件(文件不存在创建文件，文件存在清空后写入,不进行额外操作只打开也清空)
        # 'a'追加(文件最后)
        # 'x'创建（文件存在报错,不存在创建并写入内容）
        # 'r+'可读可写,默认从最后一位写入 ==>> 读写(win默认打开方式为gbk)
        # 'w+'可写可读(清空后写入) ==>> 写读
        # 'a+'可写可读(文件最后追加) ==>> 写读
        # 'x+'可写可读,文件存在报错,不存在创建并写入内容 ==>> 写读
        # 'rb'按字节读取文件
        # 'wb'按字节写文件(清空后写入)
        # 'ab'按字节追加(文件最后)
        # 'xb'文件存在报错,不存在创建并按字节写入内容
"""
# 1-1
f = open("ha.txt")  # 打开文件 ==>> 打开方式默认"只读"
data = f.read()  # 读取文件
f.close()  # 关闭文件
print(data)  # 输出
# 1-2
f = open("ha2.txt", "w")
f.write("121111111111")
f.close()

"""
操作文件:
    read()  # 无参数,读全部,有参数:b按字节;无b按字符
    tell()  # 获取当前指针位置(字节)
    seek()  # 指针跳转到指定位置(字节)
    write()  # 写数据:有b按字节,无b按字符
    close()  # 关闭
    fileno  # 文件描述符
    flush  # 强刷
    readbale  # 判断是否可读
    readline  # 仅读取一行
    truncate  # 截断数据(指针后内容清空)
    for line in **: #循环每一行
"""

"""
关闭文件:
    1.f.close
    2.用with打开操作完成自动关闭
"""

"""
用with可以一次打开多个文件
with open("文件名", '打开方式', encoding="uttf-8") as f1, open("文件名", '打开方式', encoding="uttf-8") as f2:
"""
