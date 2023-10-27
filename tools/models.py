from django.db import models

# Create your models here.
class Tools(models.Model):
    LIST_ICONS = (
        ("faWandMagicSparkles", "Simulador"),
        ("faScaleBalanced", "Comparativo"),
        ("faUserShield", "Perfil"),
        ("faCalculator", "Caluladora"),
        ("faUserNinja", "Tramite"),
    )

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    link = models.CharField(max_length=80)
    icons = models.CharField(max_length=20, choices=LIST_ICONS)
    button = models.CharField(max_length=20)
    isActive = models.BooleanField()

    class Meta:
        verbose_name_plural = "Herramientas"