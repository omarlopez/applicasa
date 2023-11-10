from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["created", "title", "description", "imgSmall", "imgLg"]

admin.site.register(Blog, BlogAdmin)
