from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer