from django.shortcuts import render
from .models import Galery
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth:user_login')
def render_gallery(request):
    print(request.user.username)
    gallerys = Galery.objects.filter(user=request.user)
    return render(request,'gallery.html')
