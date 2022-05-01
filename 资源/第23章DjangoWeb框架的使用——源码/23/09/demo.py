from django.http import HttpResponse  # 导入响应对象
import datetime  # 导入时间模块

def current_datetime(request):  # 定义一个视图方法，必须带有请求对象作为参数
    now = datetime.datetime.now()  # 请求的时间
    html = "<html><body>It is now %s.</body></html>" % now  # 生成html代码
    return HttpResponse(html)  # 将响应对象返回，数据为生成的html代码
