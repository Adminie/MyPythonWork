# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:04:16 2021

@author: Administrator
"""

import requests
import re
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
r = requests.get("https://nbviewer.jupyter.org/github/lijin-THU/notes-python/blob/master/01-python-tools/01.02-ipython-interpreter.ipynb", headers=headers)
res=etree.HTML(r.text)
 
result = res.xpath('//p/*/text()')
print(result)
