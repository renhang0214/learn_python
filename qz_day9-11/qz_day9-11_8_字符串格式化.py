# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


# 字符串格式化
# 1.百分号方式　　 % [(name)][flags][width].[precision]typecode
a = "my name is %s,age %d" % ("alex", 18)
print(a)  # my name is alex,age 18

# (name)   可选，用于选择指定的key
a = "my name is %(n1)s,age %(n2)d" % {"n1": "alex", "n2": 18}
print(a)  # my name is alex,age 18

# width    可选，占有宽度
# flags    可选，可供选择的值有:
# +     右对齐；正数前加正好，负数前加负号；(数字、字符串)
a = "my name is %(n1)+10s,age %(n2)+10d" % {"n1": "alex", "n2": 18}
print(a)  # my name is       alex,age        +18
# -     左对齐；正数前无符号，负数前加负号；(数字、字符串)
a = "my name is %(n1)-10s,age %(n2)-10d" % {"n1": "alex", "n2": 18}
print(a)  # my name is alex      ,age 18
# 空格    右对齐；正数前加空格，负数前加负号；(数字、字符串)
a = "my name is %(n1) 10s,age %(n2) 10d" % {"n1": "alex", "n2": 18}
print(a)  # my name is       alex,age         18
# 0     右对齐；正数前无符号，负数前加负号；用0填充空白处(数字)
a = "my name is %(n1)010s,age %(n2)010d" % {"n1": "alex", "n2": 18}
print(a)  # my name is       alex,age 0000000018

# .precision   可选，小数点后保留的位数
a = "my name is %s,age %.2f" % ("alex", 18)
print(a)  # my name is alex,age 18.00

# typecode 必选
# s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
a = "my name is %s! " % "alex"
print(a)  # my name is alex!
# r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
a = "my name is %r! " % "alex"
print(a)  # my name is 'alex'!
# c，整数：将数字转换成其unicode对应的值，10进制范围为0 <= i <= 1114111（py27则只支持0 - 255）；字符：将字符添加到指定位置
a = "age %c!" % 65
print(a)  # age A!
# o，将整数转换成八进制表示，并将其格式化到指定位置
a = "age %o!" % 65
print(a)  # age 101!
# x，将整数转换成十六进制表示，并将其格式化到指定位置
a = "age %x!" % 65
print(a)  # age 41!
# d，将整数、浮点数转换成十进制表示，并将其格式化到指定位置
a = "age %d!" % 65
print(a)  # age 65!
# e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
a = "age %e!" % 65
print(a)  # age 6.500000e+01!
# E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
a = "age %E!" % 65
print(a)  # age 6.500000E+01!
# f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
a = "age %.2f!" % 65
print(a)  # age 65.00!
# F，同上
a = "age %.2F!" % 65
print(a)  # age 65.00!
# g，自动调整将整数、浮点数转换成浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
a = "age %g!" % 0.000065
print(a)  # age 6.5e-05!
# G，自动调整将整数、浮点数转换成浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
a = "age %G!" % 0.000065
print(a)  # age 6.5E-05!
# % ，当字符串中存在格式化标志时，需要用 % % 表示一个百分号
a = "%s age %%20!" % "alex"
print(a)  # alex age %20!


# 2.format方式    %[(name)][flags][width].[precision]typecode
# fill           【可选】空白处填充的字符
# align        【可选】对齐方式（需配合width使用）
#     <，内容左对齐
#     >，内容右对齐(默认)
#     ＝，内容右对齐，将符号放置在填充字符的左侧，且只对数字类型有效。 即使：符号+填充物+数字
#     ^，内容居中
# sign         【可选】有无符号数字
#     +，正号加正，负号加负；
#     ，正号不变，负号加负；
#     空格 ，正号空格，负号加负；
# #            【可选】对于二进制、八进制、十六进制，如果加上#，会显示 0b/0o/0x，否则不显示
# ，            【可选】为数字添加分隔符，如：1,000,000
# width       【可选】格式化位所占宽度
# .precision 【可选】小数位保留精度
# type         【可选】格式化类型
#     传入” 字符串类型 “的参数
#         s，格式化字符串类型数据
#         空白，未指定类型，则默认是None，同s
#     传入“ 整数类型 ”的参数
#         b，将10进制整数自动转换成2进制表示然后格式化
#         c，将10进制整数自动转换为其对应的unicode字符
#         d，十进制整数
#         o，将10进制整数自动转换成8进制表示然后格式化；
#         x，将10进制整数自动转换成16进制表示然后格式化（小写x）
#         X，将10进制整数自动转换成16进制表示然后格式化（大写X）
#     传入“ 浮点型或小数类型 ”的参数
#         e， 转换为科学计数法（小写e）表示，然后格式化；
#         E， 转换为科学计数法（大写E）表示，然后格式化;
#         f ， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
#         F， 转换为浮点型（默认小数点后保留6位）表示，然后格式化；
#         g， 自动在e和f中切换
#         G， 自动在E和F中切换
#         %，显示百分比（默认显示小数点后6位）

tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')
print(tpl)

tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
print(tpl)

tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
print(tpl)

tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
print(tpl)

tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
print(tpl)

tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
print(tpl)

tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
print(tpl)

tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
print(tpl)

tpl = "i am {:s}, age {:d}".format(*["seven", 18])
print(tpl)

tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
print(tpl)

tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
print(tpl)

tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)

tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
print(tpl)

tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
print(tpl)

tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
print(tpl)
