# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')  # 获取一个zip压缩包
z.write('c1')  # 将文件添加到压缩包
z.write("c2")  # 将文件添加到压缩包
z.close()  # 关闭压缩包
# print(z.namelist())  # 获取压缩包内所有文件的名字

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
print(z.namelist())
z.extract("c1")  # 解压压缩包内指定的文件，如果文件存在则覆盖,如果不想覆盖则需要添加路径path="..."
z.extractall()  # 解压整个压缩包，如果文件存在则覆盖,如果不想覆盖则需要添加路径path="..."
z.close()

