# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import requests

r = requests.get("http://www.weather.com.cn/adat/sk/101010500.html")  # 发送get请求
r.encoding = "utf-8"  # 对给返回值进行编码
a = r.text  # 拿到返回值
print(a)
"""
{"weatherinfo":
     {"city": "怀柔",
      "cityid": "101010500",
      "temp": "9",
      "WD": "南风",
      "WS": "1级",
      "SD": "29%",
      "WSE": "1",
      "time": "10:25",
      "isRadar": "1",
      "Radar": "JC_RADAR_AZ9010_JB",
      "njd": "暂无实况",
      "qy": "1007"}
 }
"""
