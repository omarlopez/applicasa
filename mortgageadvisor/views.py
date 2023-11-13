from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mortgageadvisor.models import MortgageAdvisor, Brokers
from mortgageadvisor.serializers import MortgageAdvisorSerializer, BrokerSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from mailjet_rest import Client
import os

api_key = '355d4b31acfec48c870fff37cb40bbe3'
api_secret = '7300ab0ba16cb5097ec956fec80a8385'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')




def list_brokers(request):
    if request.method == 'GET':
        brokers =  Brokers.objects.all()
        serializer = BrokerSerializer(brokers, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def save_mortgage_advisor(request):
    if request.method == 'POST':
        #data = {
        #'FromEmail': 'applicasa.tech@gmail.com',
        #'FromName': 'Mailjet Pilot',
        #'Subject': 'APPLICASA - Activa tu cuenta',
        #'TemplateID': '5771194',
        #'TemplateLanguage': 'true',
        #'Recipients': [
		#	    {
		#		    "Email": "omarlaszloo@gmail.com"
		#	    }
		#    ]
        #}
        data = {
            "Messages": [{
                "From": {
                    "Email": "applicasa.tech@gmail.com",
                    "Name": "Mailjet Pilot"
                },
                "To": [
                    {
                        "Email": "omarlaszloo@gmail.com",
                        "Name": "passenger 1"
                    }
                ],
                "TemplateID": 1,
                "TemplateLanguage": True,
                "Subject": "Your email flight plan!"
            }]
        }
        data = JSONParser().parse(request)
        serializer = MortgageAdvisorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            result = mailjet.send.create(id=5773100,data=data)
            print(result.status_code)
            return JsonResponse(serializer.data, status=201)
            
        return JsonResponse(serializer.errors, status=400)