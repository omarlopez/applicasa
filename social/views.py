from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from social.models import Social
from social.serializers import SocialSerializer


def list_social(request):
    if request.method == 'GET':
        social = Social.objects.all()
        serializer = SocialSerializer(social, many=True)
        return JsonResponse(serializer.data, safe=False)

