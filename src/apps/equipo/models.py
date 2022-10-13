from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _


class Equipo(models.Model):
    nro_serie = models.CharField(max_length=255, primary_key=True, verbose_name=_("equipo"), help_text=_("Nro. de serie del equipo"))
    label = models.CharField(max_length=255, null=True, verbose_name=_("etiqueta"), help_text=_("Nombre de la etiqueta"))
    name = models.CharField(max_length=255, null=False, verbose_name=_("nombre"), help_text=_("Nombre del equipo asignado"))
    latitud = models.DecimalField(max_digits=8, decimal_places=6, null=True, verbose_name=_("latitud"), help_text=_("latitud"))
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name=_("longitud"), help_text=_("longitud"))
    fecha_asignacion = models.DateTimeField(auto_now_add=True,  verbose_name=_("fecha de asignación"), help_text=_(
        "fecha de asignación del equipo"))
    activo = models.BooleanField(default=False, verbose_name=_("activo"), help_text=_("equipo activo?"))
    app_eui = models.CharField(null=True, max_length=255, default="", verbose_name=_("APPEUI"), help_text=_("APPEUI de credencial"))
    app_key = models.CharField(null=True, max_length=255, default="", verbose_name=_("APPKEY"), help_text=_("APPKEY de credencial"))
    dev_eui = models.CharField(null=True, max_length=255, default="", verbose_name=_("DEVEUI"), help_text=_("DEVEUI de credencial"))

    def get_coordenadas(self):
        return "lat: {}, lng: {}".format(self.latitud, self.longitud)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("equipo")
        verbose_name_plural = "equipos"
    