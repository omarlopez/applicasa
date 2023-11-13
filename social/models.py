from django.db import models

# Create your models here.

class Social(models.Model):
    LIST_OPTIONS = (
        ("facebook", "Facebook"),
        ("X", "X"),
        ("youtube", "Youtube"),
        ("phone", "Teléfono"),
        ("whatsapp", "WhatsApp"),
        ("linkedin", "Linkedin"),
        ("Simulator", "Simulador"),
    )
    
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, choices=LIST_OPTIONS)
    link = models.CharField(max_length=50)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural = "Red Social"