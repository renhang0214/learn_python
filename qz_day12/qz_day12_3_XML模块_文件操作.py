# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang



from xml.etree import ElementTree as ET  # 导入模块并重新命名为ET

# 方法1
f = open("first.xml", "r", encoding='utf-8')

r = ET.XML(f.read())

# iter与find都是寻找的意思，iter用于寻找节点的标签，find用于寻找节点内的标签。
for n2 in r.find('country'):
    print(n2)
    """
    <Element 'rank' at 0x102220138>
    <Element 'year' at 0x102220188>
    <Element 'gdppc' at 0x1022201d8>
    <Element 'neighbor' at 0x102220228>
    <Element 'neighbor' at 0x102220278>
    """
for n2 in r.iter('country'):
    print(n2)
    """
    <Element 'country' at 0x102223908>
    <Element 'country' at 0x1022202c8>
    <Element 'country' at 0x102220458>
    """

# 方法2
r = ET.parse("first.xml")
tree_first = r.getroot()  # 获取父节点
# 修改
for i in tree_first.iter("year"):
    new_year = int(i.text) + 1
    i.text = str(new_year)  # 对xml进行更改(必须是str才能保存)
    i.set("name", "renhang")
    i.set("age", "19")
    del i.attrib["name"]  # 删除属性，因为xml文件为字典，所以删除属性时用[]括号
# 删除
for i in tree_first.iter("country"):  # 循环父节点下的country子节点
    rank = int(i.find("rank").text)  # 将rank节点的值转换为数字
    if rank > 50:
        tree_first.remove(i)  # 删除子节点

r.write("first.xml")
# i.set(a, b) 为标签添加或修改属性(a、b必须是字符串，必须传递a、b两个参数)


# 创建xml文件
# 创建根节点
r = ET.Element("famliy")

# 创建子节点
s1 = ET.Element('son', {'name': '儿1'})
s2 = ET.Element('son', {"name": '儿2'})

g1 = ET.Element('grandson', {'name': '儿11'})
g2 = ET.Element('grandson', {'name': '儿12'})
g3 = ET.Element('grandson')

# 将g1、g2两子节点分别添加到s1、s2两个子节点内，s1、s2为g1、g2的父节点
s1.append(g1)
s1.append(g2)
s1.append(g3)

# 把s1、s2两个子节点添加到根节点中，r为s1、s2的父节点
r.append(s1)
r.append(s1)

tree = ET.ElementTree(r)
tree.write('new.xml', encoding='utf-8', short_empty_elements=False,xml_declaration=True)
