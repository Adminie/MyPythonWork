from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from app1.forms import PersonForm
from app1.models import Person

def person_detail(request, pk):  # url参数pk
    try:
        p = Person.objects.get(pk=pk)  # 获取Person数据
    except Person.DoesNotExist:
        raise Http404('Person Does Not Exist')  # 获取不到抛出Http404错误页面
    return render(request, 'person_detail.html', {'person': p})  # 返回详细信息视图
