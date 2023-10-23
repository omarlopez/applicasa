from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ["created", "title", "description", "img"]

admin.site.register(Products, ProductsAdmin)

