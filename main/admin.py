from django.contrib import admin

from .models import Main


class MainAdmin(admin.ModelAdmin):
    list_display = ["created", "title", "description"]

admin.site.register(Main, MainAdmin)
