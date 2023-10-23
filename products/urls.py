from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.list_products),
]