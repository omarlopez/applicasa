from django.contrib import admin
from .models import Tools

class ToolsAdmin(admin.ModelAdmin):
    list_display=["created", "title", "description", "link", "button","icons","isActive"]

admin.site.register(Tools, ToolsAdmin)