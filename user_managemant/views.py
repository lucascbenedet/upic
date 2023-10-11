from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        password = request.POST.get('senha')
    
        if authenticate(username=user,password=password):
            return HttpResponse('LOGADO')
        
        return HttpResponse('LOGIN INVALIDO')
    
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
