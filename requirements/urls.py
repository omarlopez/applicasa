from django.urls import path
from requirements import views

urlpatterns = [
    path('requirements/', views.list_requirements),
]