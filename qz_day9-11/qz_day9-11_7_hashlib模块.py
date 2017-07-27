# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import hashlib

# md5加密
a = hashlib.md5()
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())  # 将结果作为十六进制数字字符串返回。
print(a.digest())  # 将结果作为二进制数据字符串返回。

# sha1加密
a = hashlib.sha1()
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())

# sha256加密
a = hashlib.sha256()
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())

# sha384
a = hashlib.sha384()
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())

# sha512
a = hashlib.sha512()
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())


# 严谨加密：以md5为例
a = hashlib.md5(bytes("aaa", encoding="utf-8"))
a.update(bytes('admin', encoding='utf-8'))
print(a.hexdigest())  # 将结果作为十六进制数字字符串返回。
print(a.digest())  # 将结果作为二进制数据字符串返回。


