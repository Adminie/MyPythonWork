# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:50:24 2021

@author: john
"""

import scrapy
import requests

class MySpider(scrapy.Spider):
    name = 'my'
    
    def start_requsets(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
            'http://quotes.toscrape.com/page/2/'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
     
    def parse(self, response):
        page = response.url.spilta('/')[-2]
        filename = 'my-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        

        
        




