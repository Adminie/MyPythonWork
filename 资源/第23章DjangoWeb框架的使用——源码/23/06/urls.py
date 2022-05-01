
from django.urls import re_path
from app1 import views as views
from django.urls import path
urlpatterns = [
    # 精确匹配
    path('articles/2003/', views.special_case_2003),
    # 按照正则表达式匹配4位数字年份
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # 按照正则表达式匹配4位数字年份和2位数字月份
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # 按照正则表达式匹配4位数字年份和2位数字月份和一个至少1位的slug类型的字符串
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
]

