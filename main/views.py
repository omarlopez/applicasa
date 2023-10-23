from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from main.models import Main
from main.serializers import MainSerializer 


def list_main(request):
    if request.method == 'GET':
        main = Main.objects.all()
        serializer = MainSerializer(main, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MainSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)