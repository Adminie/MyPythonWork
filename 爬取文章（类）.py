# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:29:06 2021

@author: john
"""

import requests
import re


class NovelSpider:
    
    
    
    def Get(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
        }
        
        response = requests.get(url,headers=headers)
        html=response.text
        self.html=html
        return html
    
    def Anliyse(self,html):
        p=r'<p style="text-indent: 2em;">(.*?)<div class="zdfy clearfix">'
        
        con= re.findall(p,html,re.S)[0]
        con=con.replace('<p style="text-indent: 2em;">','')
        con=con.replace('</p>','')
        return con
    def Save(self,con):
        fp = open('文章.txt', 'a')
        try:
            fp.write(con)
        except UnicodeEncodeError:
            pass
        fp.close()
    

if __name__ == '__main__':
    url="http://hm.people.com.cn/n1/2021/0823/c42272-32203857.html"
    s=NovelSpider()
    html=s.Get(url)
    con=s.Anliyse(html)
    s.Save(con)
    print(s.Anliyse(html))

