# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import shutil

'''
# 文件操作
# shutil.copyfileobj(文件1，文件2)将文件1复制（拷贝）到文件2（根据文件的打开方式，可覆盖，可追加）
shutil.copyfileobj(open("c1", "r"), open("c2", "a"))

# shutil.copyfile(文件1名,文件2名)将文件1复制（拷贝）到文件2（文件2原有内容被覆盖）
shutil.copyfile("c1", "c2")

# shutil.copymode(文件1名,文件2名)将文件1的权限复制（拷贝）到文件2
shutil.copymode("c1", "c2")

# shutil.copystat(文件1名,文件2名)将文件1的状态信息复制（拷贝）到文件2
shutil.copystat("c1", "c2")

# shutil.copy(文件1名,文件2名)将文件1的内容与权限复制（拷贝）到文件2
shutil.copy("c1", "c2")

# shutil.copy2(文件1名,文件2名)将文件1的内容与状态信息（拷贝）到文件2
shutil.copy2("c1", "c2")
'''

'''
# 文件夹操作
shutil.copytree("s1", "s2", symlinks=True, ignore=shutil.ignore_patterns("temp"), )
# s1、s2为文件夹，将s1递归复制（拷贝）到s2，s2不能存在，存在则报错。
# 参数ignore=shutil.ignore_patterns("temp")表示忽略s1中的temp文件
# 参数symlinks=True如果有快捷方式则需要写，默认False表示复制快捷方式的原文件，等于True表示创建一个新的快捷方式

shutil.rmtree("s2") # 删除为文件夹s2

shutil.move("s1", "s2")
# 递归移动文件夹
# 将文件夹s1移动到s2内，如果s2存在则将s1移动到s2内（即：s2包含s1），如果s2不存在则创建s2并将s1内的文件移动到s2（即：重命名）
'''

'''
# 压缩
shutil.make_archive("s1", "zip", )
# 创建压缩文件
# 参数base_name为将要进行压缩的文件名，也可以是文件路径/Users/macpro1/...
# 参数format为压缩包种类：zip、rar等
# 参数root_dir要进行压缩的文件夹路径,默认当前目录
# 参数owner用户，默认当前用户
# 参数group组，默认当前组
# 参数logger用户记录日志，通常是logging.logger对象
'''
