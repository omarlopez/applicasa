from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from theme.models import Theme
from theme.serializers import ThemeSerializer


def list_theme(request):
    if request.method == 'GET':
        theme = Theme.objects.all()
        serializer = ThemeSerializer(theme, many=True)
        return JsonResponse(serializer.data, safe=False)