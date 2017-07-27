# /user/bin/evn/python
# -*- coding: utf-8 -*-
# Author:Ren Hang

# a1 = 123, a2 = 456, 将a1与a2的值互换

a1 = 123
a2 = 456

temp = a1
a1 = a2
a2 = temp

print("a1:", a1, "a2:", a2)
# a1: 456 a2: 123

li = [2, 3, 45552, 212, 2343565, 13, ]
for i in range(len(li) - 1):
    if li[i] > li[i + 1]:
        temp = li[i]
        li[i] = li[i + 1]
        li[i + 1] = temp
print("li:", li)
# li: [2, 3, 212, 45552, 13, 2343565]
