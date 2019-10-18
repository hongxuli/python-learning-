from django.shortcuts import render, HttpResponse
from login import models  # 导入models文件

# Create your views here.
user_list = []

def index(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
    
