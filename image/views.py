from django.shortcuts import render,redirect
from rest_framework.generics import ListCreateAPIView
from .models import Image,Like,Comment
from .serializers import ImageSerializer,LikeSerializer,CommentSerializer,ListCommentsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
import json


def home(request):
    return render(request,'base.html')

def post_image_component(request):
    if request.method == 'GET':
        return render(request,'post_image.html')
    else:
        
        data = {
            'title' : request.POST.get('name'),
            'image' : request.FILES.get('image'),
            'user' : request.user.id
        }
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect(request,'image.html')
        return HttpResponse(json.dumps(serializer.errors))


def render_image(request,image_id):
    image = {
        'image' : Image.objects.get(id=image_id).image
    }
    return render(request,'image.html',context=image)


def like(request,post_id):
    liked = Like.objects.filter(user=request.user, image_id=post_id) 
    if liked.exists():
        liked.delete()
    else:
        like = Like(user=request.user,image_id=post_id)
        like.save()




# @api_view(['POST','DELETE'])
# def like_unlike(request,pk):
#     if request.method == 'POST':
#         serializer = LikeSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response('Impossível dar like')
#     else:
#         try:
#             like = Like.objects.get(id=pk)
#             like.delete()
#         except ValidationError:
#             return Response("Like não existe")


# @api_view(['POST'])
# def return_like_id(request):
#     try:
#         like = Like.objects.get(**request)
#         return Response({'id' : like.id})
#     except ValidationError:
#         return Response("Like não existe")


# @api_view(['POST'])
# def post_delete_comment(request,pk):
#     if request.method == 'POST':
#         serializer = CommentSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response('Não foi possível comentar')
#     else:
#         comment = Comment.objects.get(pk)
#         comment.delete()

# @api_view(['GET'])
# def list_comments(request,pk):
#     comments = Comment.objects.get(image_id=pk)
#     serializer = ListCommentsSerializer(comments)
#     return Response(serializer.data)
    

