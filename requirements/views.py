from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from requirements.models import Requirements
from requirements.serializers import RequirementsSerializer


def list_requirements(request):
    if request.method == 'GET':
        requirements = Requirements.objects.all()
        serializer = RequirementsSerializer(requirements, many=True)
        return JsonResponse(serializer.data, safe=False)