# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:03:39 2022

@author: Administrator
"""

import requests
import re



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
r = requests.get('http://zj.people.com.cn/GB/186938/186959/index.html')
p=r"<li><a href='(.*?)'"
s=r.text
n=re.findall(p,s)
for i in range(len(n)):
    url=n[i]
    resp=requests.get('http://zj.people.com.cn'+url,headers=headers)
    p1=r'<div class="box_pic"></div>(.*?)<div class="zdfy clearfix">'
    p2=r'<title>(.*?)</title>'
    resp.encoding='gbk'
    s1=resp.text
    n1=re.findall(p1,s1,re.S)[0]
    n2=re.findall(p2,s1,re.S)[0]
    n1=n1.replace('</p>\n<p>\n\t\u3000\u3000','')
    n1=n1.replace('</p>','')
    n1=n1.replace('</p>\n<p>\n\t\u3000\u3000','')
    n1=n1.replace('<p style="text-align: center;">','')
    n1=n1.replace('<span style="font-family:楷体;">','')
    print(n2,n1)