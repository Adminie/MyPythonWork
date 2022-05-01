from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app1.forms import PersonForm

def get_name(request):
    # 判断请求方法是否为POST
    if request.method == 'POST':
        # 将请求数据填充到PersonForm实例中
        form = PersonForm(request.POST)
        # 判断form是否为有效表单
        if form.is_valid():
            # 使用form.cleaned_data获取请求的数据
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # 响应拼接后的字符串
            return HttpResponse(first_name + '' + last_name)
        else:
            return HttpResponseRedirect('/error/')
    # 请求为GET方法
    else:
        return render(request, 'name.html', {'form': PersonForm()})
