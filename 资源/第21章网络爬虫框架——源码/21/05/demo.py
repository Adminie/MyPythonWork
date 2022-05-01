import requests             # 导入模块

response = requests.get('http://www.baidu.com')
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url
print(response.headers)      # 打印头部信息
print(response.cookies)      # 打印cookie信息
print(response.text)         # 以文本形式打印网页源码
print(response.content)      # 以字节流形式打印网页源码


