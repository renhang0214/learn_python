# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

import os

# os.getcwd()                 获取当前工作目录，即当前python脚本工作的目录路径
a = os.getcwd()
print("os.getcwd():", a)
# os.getcwd(): /Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9

# os.chdir("dirname")         改变当前脚本工作目录；相当于shell下cd
os.chdir("/Users/macpro1/PycharmProjects/Learn_qzkf")
a = os.getcwd()
print("os.chdir():", a)
# /Users/macpro1/PycharmProjects/Learn_qzkf

# os.curdir                   获取当前目录的字符串名: ('.')
a = os.curdir
print("os.curdir:", a)
# .

# os.pardir                   获取当前目录的父目录字符串名：('..')
a = os.pardir
print("os.pardir", a)  # ..

# os.makedirs('dir1/dir2')    可生成多层递归目录
os.makedirs("qz_day22/a1")
# os.removedirs('dirname1')   若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.removedirs("qz_day22/a1")

# os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
os.mkdir("a1")
# os.rmdir('dirname')         删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.rmdir("a1")

# os.listdir('dirname')       列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
a = os.listdir("qz_day9")
print("os.listdir():", a)
# os.listdir(): ['.DS_Store', '__pycache__', 'qz_day9_1_正则表达式.py', 'qz_day9_2_导入模块', 'qz_day9_2_模块.py', 'qz_day9_3_sys模块.py', 'qz_day9_4_os模块.py', 's1.py']

# os.remove()                 删除当前目录的指定文件
os.remove("a1.py")

# os.rename("oldname","new")  重命名文件/目录
os.rename("s1.py", "s11.py")

# os.stat('path/filename')    获取文件/目录信息
a = os.stat("/Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9")
print("os.stat():", a)
# os.stat(): os.stat_result(st_mode=16877, st_ino=8890797, st_dev=16777220, st_nlink=10, st_uid=501, st_gid=20, st_size=340, st_atime=1490079626, st_mtime=1490079641, st_ctime=1490079641)

# os.sep                      操作系统特定的路径分隔符，win下为"\\",Mac、Linux下为"/"
a = os.sep
print("os.sep:", a)
# os.sep: /

# os.linesep                  当前平台使用的行终止符，win下为"\t\n",Mac、Linux下为"\n"
a = os.linesep
a = list(a)
print("os.linesep:", a)
# os.linesep: ['\n']

# os.pathsep                  用于分割文件路径的字符串
a = os.pathsep
print("os.pathsep:", a)
# os.pathsep: :

# os.name                     字符串指示当前使用平台。win->'nt'; Mac、Linux->'posix'
a = os.name
print("os,name:", a)
# os,name: posix

# os.system("bash command")   运行shell命令，直接显示
os.system("ls")
"""
__pycache__
qz_day9_1_正则表达式.py
qz_day9_2_导入模块
qz_day9_2_模块.py
qz_day9_3_sys模块.py
qz_day9_4_os模块.py
s11.py
"""

# os.environ                  获取系统环境变量
a = os.environ
print("os.environ:", a)
# os.environ: environ({'HOME': '/Users/macpro1', 'LOGNAME': 'renhang', 'LC_CTYPE': 'zh_CN.UTF-8', 'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.6272', '__PYVENV_LAUNCHER__': '/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONUNBUFFERED': '1', 'PYCHARM_HOSTED': '1', 'SHELL': '/bin/bash', 'TMPDIR': '/var/folders/c5/47vnr1mx5wb9_8zmm1658_lm0000gn/T/', 'USER': 'renhang', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.rNAzDMsfxC/Listeners', 'PATH': '/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/3.5/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin', 'PWD': '/Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'PYTHONPATH': '/Users/macpro1/PycharmProjects/Learn_qzkf', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.H4QQ77EIBg/Render', 'XPC_FLAGS': '0x0'})

# os.path.abspath(path)       返回path规范化的绝对路径
a = os.path.abspath("qz_day9")
print("os.path.abspath():", a)
# os.path.abspath(): /Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9/qz_day9

# os.path.split(path)         将path分割成目录和文件名二元组返回
a = os.path.split("Learn_qzkf/qz_day9/qz_day9_4_os模块.py")
print("os.path.split():", a)
# os.path.split(): ('Learn_qzkf/qz_day9', 'qz_day9_4_os模块.py')

# os.path.dirname(path)       返回path的目录。其实就是os.path.split(path)的第一个元素
a = os.path.dirname("Learn_qzkf/qz_day9/qz_day9_4_os模块.py")
print("os.path.dirname():", a)
# os.path.dirname(): Learn_qzkf/qz_day9

# os.path.basename(path)      返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
a = os.path.basename("Learn_qzkf/qz_day9/qz_day9_4_os模块.py")
print("os.path.basename():", a)
# os.path.basename(): qz_day9_4_os模块.py

# os.path.exists(path)        如果path存在，返回True；如果path不存在，返回False
a = os.path.exists("/Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9")  # path必须是绝对路径，非绝对路径即使存在同样返回False
print("os.path.exists():", a)
# os.path.exists(): True

# os.path.isabs(path)         如果path是绝对路径，
a = os.path.isabs("Learn_qzkf/qz_day9/qz_day9_4_os模块.py")
print("os.path.isabs():", a)
# os.path.isabs(): False

# os.path.isfile(path)        如果path是一个存在的文件，返回True。否则返回False
a = os.path.isfile("qz_day9_4_os模块.py")  # path必须是单独的文件名或绝对路径
print("os.path.isfile():", a)
# os.path.isfile(): True

# os.path.isdir(path)         如果path是一个存在的目录，则返回True。否则返回False
a = os.path.isdir("/Users/macpro1/PycharmProjects/Learn_qzkf/qz_day9/")
print("os.path.isdir():", a)
# os.path.isdir(): True

# os.path.join(path1, path2, ...)  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
a1 = "user"
a2 = "qzkf"
a = os.path.join(a1, a2)
print("os.path.join():", a)
# os.path.join(): user/qzkf

# os.path.getatime(path)      返回path所指向的文件或者目录的最后存取时间
a = os.path.getatime("qz_day9_4_os模块.py")
print("os.path.getatime():", a)
# os.path.getatime(): 1490082789.0

# os.path.getmtime(path)      返回path所指向的文件或者目录的最后修改时间
a = os.path.getmtime("qz_day9_4_os模块.py")
print("os.path.getmtime():", a)
# os.path.getmtime(): 1490082969.0

