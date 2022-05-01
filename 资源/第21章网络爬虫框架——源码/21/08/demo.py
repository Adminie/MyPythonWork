import requests
url = 'https://www.baidu.com/'     # 创建需要爬取网页的地址
# 创建头部信息
headers = {'User-Agent':'OW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
response  = requests.get(url, headers=headers)    # 发送网络请求
print(response.content)                             # 以字节流形式打印网页源码





