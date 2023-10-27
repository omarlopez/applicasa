from django.contrib import admin
from .models import ItemRequirements, Requirements

# Register your models here.
class ItemRequirementsInLine(admin.StackedInline):
    model= ItemRequirements
    extra=1


class RequirementsAdmin(admin.ModelAdmin):
    list_display = ["created", "title", "subtitle", "isActive"]
    inlines = [ItemRequirementsInLine]

admin.site.register(Requirements, RequirementsAdmin)