from django.db import models
from apps.entidad.models import Entidad
# Create your models here.

class EmailService(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    host = models.CharField(max_length=100)
    port = models.PositiveSmallIntegerField()
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    use_tls = models.BooleanField()
    
    def __str__(self):
        return f'{self.host} ({self.user})'