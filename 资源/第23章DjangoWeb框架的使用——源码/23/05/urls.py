from app1 import views as app1_views
from django.urls import path
urlpatterns = [
    # 精确匹配视图
    path('articles/2003/', app1_views.special_case_2003),
    # 匹配一个整数
    path('articles/<int:year>/', app1_views.year_archive),
    # 匹配两个位置的整数
    path('articles/<int:year>/<int:month>/', app1_views.month_archive),
    # 匹配两个位置的整数和一个slug类型的字符串
    path('articles/<int:year>/<int:month>/<slug:slug>/', app1_views.article_detail),
]

