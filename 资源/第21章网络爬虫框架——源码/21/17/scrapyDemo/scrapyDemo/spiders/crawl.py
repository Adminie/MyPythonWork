import scrapy  # 导入框架
from scrapyDemo.items import ScrapydemoItem # 导入ScrapydemoItem类


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

    # 响应信息
    def parse(self, response):
        # 获取所有信息
        for quote in response.xpath(".//*[@class='quote']"):
            # 获取名人名言文字信息
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            # 获取作者
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            # 获取标签
            tags = quote.xpath(".//*[@class='tag']/text()").extract()
            # 创建Item对象
            item = ScrapydemoItem(text=text, author=author, tags=tags)
            yield item  # 输出信息


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

