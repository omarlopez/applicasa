from django.db import models

# Create your models here.
class Brokers(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    broker = models.CharField(max_length=100)
    description = models.CharField(max_length= 300)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural= "Catalogo Brokers"


class MortgageAdvisor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    secondLastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    broker = models.CharField(max_length=100)
    state  = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)