import requests

proxy = {'http': '122.114.31.177:808',
         'https': '122.114.31.177:8080'}  # 设置代理ip与对应的端口号
# 对需要爬取的网页发送请求
response = requests.get('http://www.mingrisoft.com/', proxies=proxy)
print(response.content)  # 以字节流形式打印网页源码







