from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from main.models import Blog
from main.serializers import BlogSerializer




class BlogViewSet(viewsets.ViewSet):

    def list(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response("Blog o'chirildi")
    
    def create(self, request):
        blog = BlogSerializer(data=request.data)
        if blog.is_valid():
            blog.save()
            return Response("Blog qo'shildi", 201)
        else:
            return Response(blog.errors)
        
    def update(self, request, pk=None):
        blog = Blog.objects.get(pk=pk)
        blog = BlogSerializer(instance=blog , data=request.data)
        if blog.is_valid():
            blog.save()
        else:
            return Response(400)
        return Response(blog.data, 200)

