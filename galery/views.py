from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Galery

def render_gallery(request):
    gallerys = Galery.objects.filter(user=request.user)
