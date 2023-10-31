from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView
from .models import Image, Like, Comment
from .serializers import (
    ImageSerializer,
    LikeSerializer,
    CommentSerializer,
    ListCommentsSerializer,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required


def home(request):
    context = {"user": request.user}
    return render(request, "index.html", context=context)


@login_required(login_url="auth:user_login")
def post_image_component(request):
    data = {
        "title": request.POST.get("name"),
        "image": request.FILES.get("image"),
        "user": request.user.id,
    }
    serializer = ImageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return redirect("image:render_image", image_id=serializer.data["id"])
    return HttpResponse(json.dumps(serializer.errors))


def render_image(request, image_id):
    if request.method == "GET":
        image_object = Image.objects.get(id=image_id)
        image = {
            "image": image_object.image,
            "image_id": image_object.id,
            "is_liked": Like.objects.filter(user=request.user, image_id=image_id),
            "comments": Comment.objects.filter(image_id=image_id).order_by("-posted"),
        }
        return render(request, "image.html", context=image)
    elif request.method == "POST":
        comment = request.POST.get("comment-field")
        user = request.user
        post = Comment.objects.create(user=user, text=comment, image_id=image_id)
        post.save()
        return redirect("image:render_image", image_id=image_id)


from django.http import JsonResponse


def like_photo(request, post_id):
    try:
        like, created = Like.objects.get_or_create(user=request.user, image_id=post_id)
        if not created:
            like.delete()
    except Exception as e:
        return JsonResponse({"error": str(e)})

    return JsonResponse({"message": "Like updated successfully"})
