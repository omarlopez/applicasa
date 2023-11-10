from django.db import models

# Create your models here.

class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    imgSmall = models.ImageField(upload_to='images/')
    imgLg = models.ImageField(upload_to='images/')
    