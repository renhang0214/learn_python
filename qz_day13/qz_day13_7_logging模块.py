# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

"""
对日志系统进行基本配置。

如果根记录器已经配置了处理程序，则此功能不起作用。
这是一种方便的方法，用于简单的脚本，用于单次配置日志记录包。
默认行为是创建一个写入sys.stderr的StreamHandler，使用BASIC_FORMAT格式字符串设置格式化程序，并将处理程序添加到根记录器中。
可以指定一些可选的关键字参数，这可以改变默认行为。

filename  文件名：使用指定的命名创建
filemode  文件的打开方式：默认为a
format    文件格式：对处理程序使用指定的格式字符串。
datefmt   日期格式：指定的日期/时间格式。(format中必须有日期，datefmt才有意义)
style     样式：如果指定了格式字符串，使用此格式指定格式字符串的类型（'％'，'{'，'$'，用于％格式化，：meth：`str.format`和：class：`string 。Template` - 默认为'％'）。
level     级别：设置日志的指定级别,默认logging=WARNING(即30)
stream    流处理器：使用指定的流初始化StreamHandler。 请注意，此参数与“filename”不兼容 - 如果两者都存在，则忽略“stream”。
handlers  处理程序：如果指定，这应该是已经创建的处理程序的一个迭代，它将被添加到根处理程序。 列表中没有分配格式化程序的任何处理程序将被分配在此函数中创建的格式化程序。

#级别：
CRITICAL = 50
FATAL = CRITICAL(50)
ERROR = 40
WARNING = 30
WARN = WARNING(30)
INFO = 20
DEBUG = 10
NOTSET = 0

注：只有【当前等级】大于【日志等级】时，日志文件才被记录。
"""

import logging

# 单个文件
logging.basicConfig(
    filename='a.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s '
           '==》 %(message)s',
    level=logging.NOTSET,
)

logging.critical('critical')
logging.error('error会计师发给我iuefjlaksakgjf')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
logging.log(10, 'log')

# 多个文件
# 定义文件
file_1_1 = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')  # 创建文件
file_1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')

fmt = logging.Formatter(fmt="Time:%(asctime)s - name:%(name)s - %(levelname)s -%(module)s:  %(message)s")  # 创建文件格式

file_1_1.setFormatter(fmt)  # 将创建的格式应用到文件
file_1_2.setFormatter(fmt)

# fmt = logging.Formatter()

# 定义日志
logger1 = logging.Logger('s1', level=logging.ERROR)
logger1.addHandler(file_1_1)
logger1.addHandler(file_1_2)

logger2 = logging.Logger('s2', level=logging.INFO)
logger2.addHandler(file_1_1)

# 写日志
logger1.critical('1111')  # 因为logger1将file_1_1.log与file_1_2.log都加进去了，所以分别写入两个文件
logger2.error("ksjdhfowilfnkjsb")  # 因为logger2只将file_1_1.log加进去了，所以只写入file_1_1.log
