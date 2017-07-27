# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import tarfile

# 压缩
tar = tarfile.open('your.tar','w')  # 创建一个压缩包
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')  # 将文件添加到压缩包并命名
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')  #
tar.close()  # 关闭压缩包

# 解压
tar = tarfile.open('your.tar','r')  # 打开一个压缩包
tar.extractall()  # 解压包内所有文件（可设置解压地址）
tar.close()  # 关闭压缩包

