from django.urls import path
from social import views

urlpatterns = [
    path('social/', views.list_social),
]