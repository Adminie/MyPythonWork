import requests
# 导入requests.exceptions模块中的三种异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException
# 循环发送请求50次
for a in range(1, 50):
    try:    # 捕获异常
        # 设置超时为0.5秒
        response = requests.get('https://www.baidu.com/', timeout=0.5)
        print(response.status_code)                                        # 打印状态码
    except ReadTimeout:                                                    # 超时异常
        print('timeout')
    except HTTPError:                                                      # HTTP异常
        print('httperror')
    except RequestException:                                               # 请求异常
        print('reqerror')






