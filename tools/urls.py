from django.urls import path
from tools import views

urlpatterns = [
    path('tools/', views.list_tools),
]