from django.urls import path
from theme import views

urlpatterns = [
    path('theme/', views.list_theme),
]