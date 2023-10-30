from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .serializers import UserSerializer
from .forms import UserForm
from image.models import Image

def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')
    elif request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('senha')

        user = authenticate(request,username=username, password=password)
    
        if user:
            login(request, user=user)
            return redirect('image:home')
        else:
            return render(request,'user_login.html', context={'errors' : 'Invalid username or password',
                                                              'username' : username})
        
    
def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request,'register.html',{'form' : form})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('image:home')
        else:
            return render(request, 'register.html', {'form' : form})
        

def profile(request):

    context = {
        'user_images' : Image.objects.filter(user=request.user)
    }
    return render(request,'profile.html',context=context)

def user_logout(request):
    logout(request)
    return redirect('auth:user_login')
