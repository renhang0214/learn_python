# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import requests
from xml.etree import ElementTree as ET  # 导入模块并重新命名为ET

# 验证qq在线状态
r = requests.get(
    'http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=725367')  # 发送get请求
a = r.text  # 拿到返回值

n = ET.XML(a)  # 获得xml格式对象（将返回值XML格式化）
if n.text == "Y":  # 获取标签中间的内容
    print("在线")
else:
    print("离线")

# 查看列车时刻表
r = requests.get(
    'http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
r = r.text  # # 拿到返回值
# print(r)
# 解析XML格式内容
n = ET.XML(r)  # 获得xml格式对象（将返回值XML格式化）
for i in n.iter('TrainDetailInfo'):
    print(i.find('TrainStation').text, i.find('StartTime').text, i.tag, i.attrib)
    # n.iter('TrainDetailInfo') 寻找节点：TrainDetailInfo = 标签名，寻找标签名叫 TrainDetailInfo 的节点
    # i.attrib  获取标签属性：
    # i.find('TrainStation')   寻找标签：
    # i.find('TrainStation').text   获取标签的内容


"""
西安北（车次：G666） 15: 58:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '0',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo1',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
渭南北
16: 17:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '1',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo2',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
三门峡南
17: 01:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '2',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo3',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
洛阳龙门
17: 34:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '3',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo4',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
郑州东
18: 20:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '4',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo5',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
安阳东
19: 03:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '5',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo6',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
邯郸东
19: 22:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '6',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo7',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
石家庄
20: 11:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '7',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo8',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
高碑店东
21: 01:00
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '8',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo9',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
北京西
None
TrainDetailInfo
{'{urn:schemas-microsoft-com:xml-msdata}rowOrder': '9',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}id': 'TrainDetailInfo10',
 '{urn:schemas-microsoft-com:xml-diffgram-v1}hasChanges': 'inserted'}
"""
print(n.tag)  # 获取根节点
# {http://WebXml.com.cn/}DataSet
