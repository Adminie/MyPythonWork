import requests
# 循环发送请求50次
for a in range(1, 50):
    try:    # 捕获异常
        # 设置超时为0.5秒
        response = requests.get('https://www.baidu.com/', timeout=0.5)
        print(response.status_code)                                        # 打印状态码
    except Exception as e:                                                 # 捕获异常
        print('异常'+str(e))                                                # 打印异常信息






