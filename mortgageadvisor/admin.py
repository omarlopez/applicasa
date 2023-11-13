from django.contrib import admin
from .models import MortgageAdvisor, Brokers


class BrokersAdmin(admin.ModelAdmin):
    list_display = ["created", "broker", "description"]
    model = Brokers
    

class MortgageAdmin(admin.ModelAdmin):
    list_display = ["fullName", "lastName", "secondLastName", "email", "broker", "state", "phone"]

admin.site.register(MortgageAdvisor, MortgageAdmin)
admin.site.register(Brokers, BrokersAdmin)