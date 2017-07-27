# !/usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

"""
njksdk,smacboasehfk,nw

"""

print(vars())
# {'__file__': '/Users/macpro1/PycharmProjects/Learn_qzkf/qz_day12/qz_day12_1_模块1补充.py',
# '__doc__': None,
# '__cached__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1005a5d68>,
# '__package__': None,
# '__builtins__': <module 'builtins' (built-in)>,
# '__name__': '__main__',
# '__spec__': None}
print(__doc__)  # njksdk,smacboasehfk,nw

a = '("11","22","33","alex")'
import json
a = json.loads(a)
print(a)


