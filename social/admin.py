from django.contrib import admin
from .models import Social

class SocialAdmin(admin.ModelAdmin):
    list_display=["created", "name", "link", "isActive"]

admin.site.register(Social, SocialAdmin)