from django.shortcuts import render # type: ignore
from .models import Posts
from rest_framework import viewsets
from .serializers import PostSerializer

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-created_at')
    serializer_class = PostSerializer