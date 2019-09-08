from django.http import HttpResponse

def index(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse('我的第一个about页面')

def add():
    pass
