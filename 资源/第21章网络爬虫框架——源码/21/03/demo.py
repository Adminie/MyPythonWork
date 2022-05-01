import urllib3

# 创建PoolManager对象，用于处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 对需要爬取的网页发送请求
response = http.request('GET','https://www.baidu.com/')
print(response.data)     #打印读取内容


