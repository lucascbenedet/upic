<<<<<<< HEAD
from django.shortcuts import render
from .models import Galery
from django.contrib.auth.decorators import login_required

@login_required(login_url='auth:user_login')
def render_gallery(request):
    print(request.user.username)
    gallerys = Galery.objects.filter(user=request.user)
    return render(request,'gallery.html')
=======
from django.shortcuts import render,redirect,get_object_or_404 
from django.contrib.auth.decorators import login_required
from .models import Galery
from rest_framework.generics import RetrieveDestroyAPIView
from .serializers import GallerySerializer

@login_required(login_url='auth:user_login')
def create_gallery(request):
    name = request.POST.get('name')
    gallery = Galery.objects.create(name=name,user=request.user)
    gallery.save()
    return redirect('gallery:gallery-page') 

@login_required(login_url='auth:user_login')
def gallery_page(request):
    context = {
        'gallerys' : Galery.objects.filter(user=request.user)
    }
    return render(request,'gallery.html',context=context)

def render_gallery(request, pk):
    queryset = Galery.objects.filter(user=request.user)
    context = {
        'gallery' : get_object_or_404(queryset, pk=pk)
    }
    return render(request,'image_gallery.html',context=context)

def delete_gallery(request, pk):
    queryset = Galery.objects.filter(user=request.user)
    instance = get_object_or_404(queryset, pk=pk)
    instance.delete()
    return redirect('gallery:gallery-page') 



>>>>>>> 87427c519e435404e99e885966fd686974a5239e
