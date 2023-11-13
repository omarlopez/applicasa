from django.urls import path
from mortgageadvisor import views
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework  import routers

urlpatterns = [
    path('api/v1/mortgageadvisor/', views.save_mortgage_advisor),
    path('api/v1/list-brokers/', views.list_brokers),
]