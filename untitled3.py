# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:39:41 2021

@author: john
"""

import scrapy


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
        filename = 'quotes-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        
        
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__=='__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('my')
    process.start()
    