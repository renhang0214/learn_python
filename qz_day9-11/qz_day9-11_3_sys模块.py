# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# sys模块
import sys
import time

# sys.argv  用于获取用户给脚本传入的参数（命令行参数List，第一个元素是程序本身路径）
# sys.exit(n)   退出，参数n为退出时输出的内容，可不写
# sys.platform  返回操作系统的版本
# sys.version   python版本
# sys.maxint    最大Int值
# sys.path    返回模块导入时寻找的地址
a = sys.path
# print(a)
for i in a:
    print(i)
# PyCharm中第二条地址为Py寻找模块地址的过程，导入模块时寻找的地址，在Charm自动添加的，在终端等运行时无第二条地址

print("\n")


# 进度条
# sys.stdout.flush()  清空输出，强制刷新
# sys.sydout.write(r)  不加换行符
# \r 回到当前的首个位置

def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = "\r%s>> %d%%" % ("=" * num, rate_num)  # 有进度条
    sys.stdout.write(r)
    sys.stdout.flush()
    return view_bar


for i in range(0, 101):
    time.sleep(0.1)
    view_bar(i, 100)

print("\n")

def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    # r = "\r%d%%" % rate_num  # 无进度条
    r = "\r%s>%d%%" % ("=" * num, rate_num)  # 有进度条

    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.3)
        view_bar(i, 100)
print(sys.platform)
