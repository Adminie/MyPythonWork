# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 20:32:18 2021

@author: Administrator
"""

import requests
import re



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
r = requests.get("https://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/index.ipynb", headers=headers)
p1=r'<li><a href="(.*?)>.*?</a></li>'
s=r.text
n1=re.findall(p1,s)
for i in range(7,len(n1)):
    url=n1[i]
    
    resp=requests.get('https://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/'+'url',headers=headers)
    p=r'<p>(.*?)</p>'
    res =re.findall(p,resp.text,re.S)
    for i in range(0,len(res)-6):
        rs=res[i]
        rs=rs.replace('</code>','')
        rs=rs.replace('<strong>','')
        rs=rs.replace('<code>','')
        rs=rs.replace('</strong>','')
        print(rs)
    