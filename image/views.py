from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Image,Like,Comment
from .serializers import ImageSerializer,LikeSerializer,CommentSerializer,ListCommentsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError


def home(request):
    return render(request,'base.html')

def image_view(request):
    image = {
        'image' : Image.objects.get(user=1).image
    }
    return render(request, 'image.html',context=image)

@api_view(['POST'])
def post_image(request):
    request.data['user'] = request.user.id
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Upload concluído')
    return Response(serializer.errors)


@api_view(['POST','DELETE'])
def like_unlike(request,pk):
    if request.method == 'POST':
        serializer = LikeSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Impossível dar like')
    else:
        try:
            like = Like.objects.get(id=pk)
            like.delete()
        except ValidationError:
            return Response("Like não existe")


@api_view(['POST'])
def return_like_id(request):
    try:
        like = Like.objects.get(**request)
        return Response({'id' : like.id})
    except ValidationError:
        return Response("Like não existe")


@api_view(['POST'])
def post_delete_comment(request,pk):
    if request.method == 'POST':
        serializer = CommentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Não foi possível comentar')
    else:
        comment = Comment.objects.get(pk)
        comment.delete()

@api_view(['GET'])
def list_comments(request,pk):
    comments = Comment.objects.get(image_id=pk)
    serializer = ListCommentsSerializer(comments)
    return Response(serializer.data)
    

