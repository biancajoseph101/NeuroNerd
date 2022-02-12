from django.shortcuts import render

from .models import Tag, Post, Resource, ResourceType
from rest_framework import generics
from .serializers import TagSerializer, PostSerializer, UserSerializer, ResourceSerializer, ResourceTypeSerializer
from accounts.models import CustomUser


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ResourceList(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceTypeList(generics.ListCreateAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer


class ResourceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
