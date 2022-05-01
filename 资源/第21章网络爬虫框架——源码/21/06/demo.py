import requests

data = {'word': 'hello'}  # 表单参数
# 对需要爬取的网页发送请求
response = requests.post('http://httpbin.org/post', data=data)
print(response.content)     # 以字节流形式打印网页源码


