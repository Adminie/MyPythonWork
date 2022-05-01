import scrapy  # 导入框架
import twisted


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 定义爬虫名称

    def start_requests(self):
        # 设置爬取目标的地址
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        # 获取所有地址，有几个地址发送几次请求
        for url in urls:
            # 发送网络请求
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 获取页数
        page = response.url.split("/")[-2]
        # 根据页数设置文件名称
        filename = 'quotes-%s.html' % page
        # 写入文件的模式打开文件，如果没有该文件将创建该文件
        with open(filename, 'wb') as f:
            # 像文件中写入获取的html代码
            f.write(response.body)
        # 输出保存文件的名称
        self.log('Saved file %s' % filename)
# 导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess
# 导入获取项目设置信息
from scrapy.utils.project import get_project_settings


# 程序入口
if __name__=='__main__':
    # 创建CrawlerProcess类对象并传入项目设置信息参数
    process = CrawlerProcess(get_project_settings())
    # 设置需要启动的爬虫名称
    process.crawl('quotes')
    # 启动爬虫
    process.start()

