import urllib.request  # 导入模块

# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()  # 读取网页代码
print(html)              # 打印读取内容
