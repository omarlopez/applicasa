from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from tools.models import Tools
from tools.serializers import ToolsSerializer


def list_tools(request):
    if request.method == 'GET':
        tools = Tools.objects.all()
        serializer = ToolsSerializer(tools, many=True)
        return JsonResponse(serializer.data, safe=False)
