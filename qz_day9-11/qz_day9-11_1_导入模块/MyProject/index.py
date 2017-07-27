# /user/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 7.导入文件夹内py文件模块的三种方法
# 方法1：
from lib.account import login

login()

# 方法2：
from lib import account

account.login()

# 方法3：
import lib.account

lib.account.login()

# 8.设置别名：
from lib import account as xxx

xxx.login()

# 9.导入制定文件夹（/Users/macpro1/Documents）下的py文件
import sys

sys.path.append("/Users/macpro1/Documents")
import buy

ret = buy.func()
print(ret)
# /Users/macpro1/Documents
# for i in sys.path:
#     print(i)