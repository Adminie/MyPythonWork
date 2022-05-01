from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from app1.forms import PersonForm
from app1.models import Person

class PersonFormView(View):
    form_class = PersonForm  # 定义表单类
    initial = {'key': 'value'}  # 定义表单初始化展示参数
    template_name = 'name.html'  # 定义渲染的模板

    def get(self, request, *args, **kwargs):  # 定义GET请求的方法
        # 渲染表单
        return render(request, self.template_name,
                          {'form': self.form_class(initial=self.initial)})

    def post(self, request, *args, **kwargs):  # 定义POST请求的方法
        form = self.form_class(request.POST)  # 填充表单实例
        if form.is_valid():  # 判断请求是否有效
            # 使用form.cleaned_data获取请求的数据
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # 响应拼接后的字符串
            return HttpResponse(first_name + '' + last_name)  # 返回拼接的字符串
        return render(request, self.template_name, {'form': form})  # 如果表单无效，返回表单

