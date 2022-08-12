from django.shortcuts import render

# Create your views here.

def index1(request):
    ans = {}  # 创建一个字典
    ans['head'] = 'hello world'  # 赋值
    return render(request, 'mainAnalysis/firstpage.html', ans)  # 输出字典