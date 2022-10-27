from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.usuario.models import Usuario

ROL_SELECCION = (
    (1, 'ADMINISTRADOR'),
    (2, 'MONITOR'),
)


class Entidad(models.Model):
    nombre = models.CharField(max_length=255, verbose_name=_("nombre"), help_text=_("Nombre de la entidad"))
    is_active = models.BooleanField(default=False, verbose_name=_("activo"), help_text=_(
        "Es una entidad activa?"))

    # logo = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("entidad")
        verbose_name_plural = "entidades"


class Miembro(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name=_("fecha de asignación"), help_text=_(
        "fecha de asignación del miembro a entidad"))
    activo = models.BooleanField(default=False,verbose_name=_("activo"), help_text=_(
        "Es un miembro activo?"))
    rol = models.PositiveSmallIntegerField(choices=ROL_SELECCION, verbose_name=_("rol"),

                                           help_text=_(
                                               "Indica el Rol de un Miembro en la Entidad"))

    class Meta:
        verbose_name = _("miembro")
        verbose_name_plural = "miembros"
