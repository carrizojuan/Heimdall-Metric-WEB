from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.equipo.models import Equipo


class Medidor(models.Model):
    
    nro_cliente = models.IntegerField()
    nro_suministro=models.IntegerField()
    nro_serie= models.ForeignKey(Equipo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("medidor")
        verbose_name_plural = "medidores"
        db_table = "medidor"
