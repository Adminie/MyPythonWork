# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:04:21 2021

@author: john
"""

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
r = requests.get("http://hm.people.com.cn/n1/2021/0823/c42272-32203857.html", headers=headers)
#用正则匹配两节点之间的内容，中间用（.*?）
p1=r'<p style="text-indent: 2em;">(.*?)<div class="zdfy clearfix">'
s=r.text
n1=re.findall(p1,s,re.S)[0]

#清洗多余字符
n1=n1.replace('<p style="text-indent: 2em;">','')
n1=n1.replace('</p>','')
print(n1)