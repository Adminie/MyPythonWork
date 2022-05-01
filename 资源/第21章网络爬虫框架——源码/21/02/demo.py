import urllib.parse
import urllib.request

# 将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
html = response.read()  # 读取网页代码
print(html)             # 打印读取内容

