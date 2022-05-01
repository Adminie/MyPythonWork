# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:06:17 2021

@author: john
"""

import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
r = requests.get("http://opinion.people.com.cn/n1/2021/0813/c223228-32192755.html", headers=headers)
p1=r'\w([^a-zA-Z\d\\"",.:;{}<>=\?\-/])'
s=r.text
n1=re.findall(p1,s)
for i in n1:
    print(i,end='')


