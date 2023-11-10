from django.db import models

# Create your models here.

class Theme(models.Model):

    LIST_ALIGN = (
        ("izquierda", "izquierda"),
        ("centrado", "centrado"),
        ("derecha", "derecha")
    )

    created = models.DateTimeField(auto_now_add=True)
    headerColor = models.CharField(max_length=100)
    tileColor = models.CharField(max_length=50)
    titleSize = models.CharField(max_length=20)
    subTitleColor = models.CharField(max_length=20)
    subTitleSize = models.CharField(max_length=20)
    titleBySecctionColor = models.CharField(max_length=20)
    titleBySecctionSize = models.CharField(max_length=20)
    titleBySecctionAlign = models.CharField(max_length=30, choices=LIST_ALIGN)
    colorFooter = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Tema"