from django.db import models

# Create your models here.
class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
