from django.urls import path
from main import views

urlpatterns = [
    path('main/', views.list_main)
]