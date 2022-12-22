import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.equipo.models import Equipo


class Medidor(models.Model):
    nro_cliente = models.UUIDField(null=True, default=uuid.uuid4, verbose_name=_("Nro. Cliente"), help_text=_("Número de Cliente"))
    nro_suministro = models.IntegerField(null=True, verbose_name=_("Nro. suministro"),
                                         help_text=_("Número de suministro"))
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, null=False, verbose_name=_("Equipo"),
                               help_text=_("Equipo"))
    fecha_asignacion = models.DateTimeField(auto_now_add=True,  verbose_name=_("fecha de asignación"), help_text=_(
        "fecha de asignación del medidor"))

    class Meta:
        verbose_name = _("medidor")
        verbose_name_plural = "medidores"
        db_table = "medidor"
        unique_together = ('nro_cliente', 'nro_suministro','equipo')
        
