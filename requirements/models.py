from django.db import models

class Requirements(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural = "Requisitos"

class ItemRequirements(models.Model):
    main = models.ForeignKey(Requirements, related_name='main', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description= models.CharField(max_length=100)
    isActive= models.BooleanField()