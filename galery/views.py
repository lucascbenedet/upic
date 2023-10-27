from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Galery

def render_gallery(request):
    print(request.user.username)
    gallerys = Galery.objects.filter(user=request.user)
    return render(request,'gallery.html')
