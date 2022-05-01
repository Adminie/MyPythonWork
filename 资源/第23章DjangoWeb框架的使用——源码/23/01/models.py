from django.db import models  # 引入django.db.models模块
class Person(models.Model):
    """
    编写Person模型类，数据模型应该继承于models.Model或其子类
    """
    # 第一个字段使用models.CharField类型
    first_name = models.CharField(max_length=30)
    # 　第二个字段使用models.CharField类型
    last_name = models.CharField(max_length=30)

