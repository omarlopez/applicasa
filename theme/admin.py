from django.contrib import admin
from .models import Theme


class ThemeAdmin(admin.ModelAdmin):
    list_display=["created", "headerColor", "tileColor", "titleSize", "subTitleColor", "subTitleSize"]

admin.site.register(Theme, ThemeAdmin)