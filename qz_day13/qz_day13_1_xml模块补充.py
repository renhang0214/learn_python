# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


from xml.etree import ElementTree as ET  # 导入模块并重新命名为ET
from xml.dom import minidom

# 用方法1更改xml文件
f = open("first.xml", "r", encoding='utf-8')

tree_first = ET.XML(f.read())  # 获取根节点

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

r = ET.ElementTree(tree_first)  # 新的xml对象（因为之前的才做都在内存，需要建一个对象才可以写入）
r.write("first.xml")


# i.set(a, b) 为标签添加或修改属性(a、b必须是字符串，必须传递a、b两个参数)


# 美化 给xml文件添加缩进
def prettify(tree):
    """
    美化，给xml文件添加缩进，
    :param tree:
    :return:
    """
    r = ET.tostring(tree, encoding="utf-8")  # 将根节点转换为字符串
    a = minidom.parseString(r)  # 将字符串转换为minidom对象
    return a.toprettyxml(indent="\t")


# 创建xml文件
# 创建根节点
r = ET.Element("family")

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

new_tree = prettify(r)
f = open("new.xml", "w", encoding='utf-8')
f.write(new_tree)
f.close()

# 用前缀来避免命名冲突（命名空间）
ET.register_namespace('com', "http://www.company.com")  # com为前缀的简写，"http://www.company.com"为前缀

# 构建树结构
r = ET.Element("{http://www.company.com}STUFF")  # STUFF为标签名
s = ET.SubElement(r, "{http://www.company.com}MORE_STUFF", attrib={"{http://www.company.com}hhh": "123"})
s.text = "STUFF EVERYWHERE!"

# 创建一个XML对象并将根节点传入
tree = ET.ElementTree(r)

tree.write("page.xml", xml_declaration=True, encoding='utf-8', method="xml")
''''
<?xml version='1.0' encoding='utf-8'?>
<com:STUFF xmlns:com="http://www.company.com">
    <com:MORE_STUFF com:hhh="123">STUFF EVERYWHERE!</com:MORE_STUFF>
</com:STUFF>
'''

# 创建XML文件的方法2   makeelement
# 创建根节点
root = ET.Element("famliy")

# 创建大儿子
# son1 = ET.Element('son', {'name': '儿1'})
son1 = root.makeelement('son', {'name': '儿1'})
# 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
son2 = root.makeelement('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
grandson2 = son1.makeelement('grandson', {'name': '儿12'})

son1.append(grandson1)
son1.append(grandson2)

# 把儿子添加到根节点中
root.append(son1)
root.append(son1)

tree = ET.ElementTree(root)
tree.write('oooo.xml', encoding='utf-8', short_empty_elements=False)

# 创建XML文件的方法3   SubElement
from xml.etree import ElementTree as ET

# 创建根节点
root = ET.Element("famliy")

# 创建节点大儿子
son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# 创建小儿子
son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})

# 在大儿子中创建一个孙子
grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
grandson1.text = '孙子'

et = ET.ElementTree(root)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)
