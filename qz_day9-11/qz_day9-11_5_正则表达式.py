# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

# RE模块
import re

# #基本语法
# match  ==》 匹配开头
# 终端
a = re.match("a", "asjkaakjsh")
a.group  # 打印，输出
# PyCharm
a = re.match("a", "asjkaakjsh").group()
print("1-match:", a)
# search  ==》 找到第一个
# 终端
a = re.search("a", "asjkaakjsh")
a.group()
# PyCharm
a = re.search("a", "asjkaakjsh").group()
print("2-secrch:", a)

# findall  ==》 匹配所有
# 终端
re.findall("a", "asjkaakjsh")
# PyCharm
a = re.findall("a", "asjkaakjsh")
print("3-findall:", a)

# split  ==》 匹配分割
# 终端
re.split("a", "asjkaakjsh")
# PyCharm
a = re.split("a", "asjkaakjsh")
print("4-aplit:", a)

# sub  ==》 匹配替换
# 终端
re.sub("a", "A", "asjkaakjsh")
# PyCharm
a = re.sub("a", "A", "asjkaakjsh")
print("5-sub:", a)

# #字符匹配
# . 匹配任意（除\n以外）的字符
a = re.search("a.", "asjkaakjsh").group()
print("6-'.':", a)  # 6-'.': as
# ^ 匹配以字符开头
a = re.search("^a", "asjkaakjsh").group()
print("7-'^':", a)  # 7-'^': a
# + 匹配符号前一个字符1~n次，通常按照最大的匹配，符号后面加一个？按照最小的匹配
a = re.search("a+", "asjkaakjsh").group()
print("8-'+':", a)  # 8-'+': a
# $ 匹配字符结尾
a = re.search("a$", "asjkaakjsh lia")
b = a.group()
print("9-'$':", b)  # 9-'$': a
# * 匹配符号前的一个字符0~n次，代表所有
a = re.findall("a*", "asjkaakjsh lia")
print("10-'*':", a)
# 10-'$': ['a', '', '', '', 'aa', '', '', '', '', '', '', '', 'a', '']
# ? 匹配符号前的一个字符0~1次
a = re.findall("a?", "asjkaakjsh lia")
print("11-'?':", a)
# 11-'?': ['a', '', '', '', 'a', 'a', '', '', '', '', '', '', '', 'a', '']
# {m}    匹配符号前的一个字符m次
a = re.search("a{2}", "asjkaakjsh lia").group()
print("12-'{}':", a)  # 12-'{}': aa
# {n,m} 匹配符号前的一个字符n~m次
a = re.search("a{0,2}", "asjkaakjsh lia").group()
print("13-'{}':", a)  # 13-'{}': a
# | 匹配符号的两侧其中一个条件即可
a = re.search("a|j", "asjkaakjsh lia").group()
print("14-'|':", a)  # 14-'|': a
# []
# #[nm]或，匹配符号内n或m
a = re.search("[ja]", "asjkaakjsh lia").group()
print("15-'[]':", a)  # 15-'[]': a
# #[元字符]，匹配字符本身（除个别符号外），无特殊意义，[a.b]==>a.b
a = re.search("a[.]a", "asjka.akjsh lia").group()
print("16-'[]':", a)  # 16-'[]': a.a
# #[n-m]至，匹配n~m
a = re.search("a[a-k]", "asjka.akjsh lia").group()
print("17-'[]':", a)  # 17-'[]': ak
# #[^]非
a = re.search("a[^a-k]", "asjka.akjsh lia").group()
print("18-'[]':", a)  # 18-'[]': as
# [\]同\，具有特殊意义
a = re.findall("a[\d]", "asjka\dkjsh lia")
print("19-'[]':", a)  # 19-'[]': []  "\d具有特殊意义"
# ()    分组匹配
a = re.search("(abc){2}a(123|456)c", "abcabca456c").group()
print("20-'()':", a)  # 20-'()': abcabca456c
# \ ⓵后面紧跟元字符表示去掉特殊功能;⓶后面紧跟普通字符表示实现特殊功能呢;⓷后面紧跟数字实现分组
# \A    只从字符开头匹配
a = re.search("\Aalex", "alexhsjdgf").group()
print("21-'\\':", a)  # 21-'': alex
# \Z    匹配字符结尾，同$
a = re.search("alex\Z", "hsjdgfalex").group()
print("22-'\\':", a)  # 22-'\': alex
# \d    匹配10进制的数字，同[0-9]
a = re.search("\d", "hs2jdg3fal4ex").group()
print("23-'\\':", a)  # 23-'\': 2
# \D    匹配非数字，同[^0-9]
a = re.search("\D", "hs2jdg3fal4ex").group()
print("24-'\\':", a)  # 24-'\': h
# \w    匹配字母与数字，同[0-9a-zA-Z]
a = re.findall("\w", "hs2jdg3fal4ex")
print("25-'\\':", a)  # 25-'\': ['h', 's', '2', 'j', 'd', 'g', '3', 'f', 'a', 'l', '4', 'e', 'x']
# \W   匹配非字符数字，同[^0-9a-zA-Z]
a = re.findall("\W", "hs2 jd.g3\t?fa\l4\nex")
print("26-'\\':", a)  # 26-'\': ['.', '?', '\\']
# \s    匹配空格\t\n\r等，同[\t\n\r\f\v]
a = re.findall("\s", "h2 j.g3\t?\l4\n")
print("27-'\\':", a)  # 27-'\': [' ', '\t', '\n']
# \S    匹配非空格\t\n\r等，同[^\t\n\r\f\v]
a = re.findall("\S", "h2 j.g3\t?\l4\n")
print("28-'\\':", a)  # 28-'\': ['h', '2', 'j', '.', 'g', '3', '?', '\\', 'l', '4']
# \b    匹配单词边界，即单词和空格之间的位置
a = re.findall(r'e\b', 'my name is ')
print("29-'\b':", a)  # 29-': ['e']

# 示例：分组匹配（身份证）（取到字典）
a = re.search("(?P<provice>[0-9]{3})(?P<city>[0-9]{3})(?P<brithday>[0-9]{8})", "210726199001010101").groupdict()
print("30-'()'：", a)  # 30-'()'： {'provice': '210', 'brithday': '19900101', 'city': '726'}

a = re.search("([0-9]{3})([0-9]{3})([0-9]{8})", "210726199001010101").groups()  # [0-9]等同\d
print("31-'()'：", a)  # 31-'()'： ('210', '726', '19900101')

# re.I 忽略大小写
a = re.search("[a-z]", "My name is Alex").group()
print("32-'re.I':", a)  # 32-'re.I': y
a = re.search("[a-z]", "My name is Alex", flags=re.I).group()
print("33-'re.I':", a)  # 33-'re.I': M

# re.S 任意匹配
a = re.search(".+", "My name\n is Alex").group()
print("34-'re.I':", a)  # 34-'re.I': My name
a = re.search(".+", "My name is Alex", flags=re.S).group()
print("35-'re.I':", a)  # 35-'re.I': My name is Alex

# 补充
# finditer  ==》 匹配所有
# 终端
re.finditer("a", "asjkaakjsh")
# PyCharm
a = re.finditer("a", "asjkaakjsh")
print("36-finditer:", a)
for i in a:
    print(i, "group:", i.group(), "groups:", i.groups(), "groupdict:", i.groupdict())

# 36-finditer: <callable_iterator object at 0x1021cd5f8>
# <_sre.SRE_Match object; span=(0, 1), match='a'> group: a groups: () groupdict: {}
# <_sre.SRE_Match object; span=(4, 5), match='a'> group: a groups: () groupdict: {}
# <_sre.SRE_Match object; span=(5, 6), match='a'> group: a groups: () groupdict: {}