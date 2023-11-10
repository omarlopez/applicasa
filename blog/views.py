from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.models import Blog
from blog.serializers import BlogSerializer

def list_blog(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return JsonResponse(serializer.data, safe=False)