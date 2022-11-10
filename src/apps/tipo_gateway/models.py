from django.db import models
from django.utils.translation import gettext_lazy as _


class TipoGateway(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_("nombre"), help_text=_("Nombre del tipo de gateway"))

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("tipo_gateway")
        verbose_name_plural = "tipo_gateways"
