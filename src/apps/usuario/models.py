from cgi import print_form
import uuid
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Usuarios deben tener un correo electrónico válido')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('nombre_usuario', "Admin")
        extra_fields.setdefault('nombres', "Admin")
        extra_fields.setdefault('apellidos', "Admin")
        if extra_fields.get('is_staff') is not True:
            raise ValueError('EL superusuario debe tener  is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('EL Superusuario debe tener  is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    """PermissionsMixin contiene los siguientes campos:
        - `is_superuser`
        - `grous`
        - `user_permissions`
     """
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    nombre_usuario = models.CharField(max_length=100, unique=True, verbose_name=_("nombre usuario"), help_text=_(
        "Nombre del Usuario en el sistema"
    ))

    nombres = models.CharField(max_length=200, verbose_name=_("nombres"), help_text=_(
        "Nombres de la Persona"
    ))

    apellidos = models.CharField(max_length=200, verbose_name=_("apellidos"), help_text=_(
        "Apellidos de la Persona"
    ))

    email = models.EmailField(
        verbose_name=_("correo electrónico"), unique=True,
        error_messages={
            'unique': _(
                "Un usuario ya está registrado con esta dirección de correo electrónico")})

    is_staff = models.BooleanField(
        verbose_name=_("staff"), default=False,
        help_text=_("Designa si el usuario puede iniciar sesión en este sitio de administración. True = Administrador False = Monitoreo"))

    is_active = models.BooleanField(
        verbose_name=_("activo"), default=False, help_text=_(
            "Designa si este usuario debe ser tratado como activo."
            "Anule la selección de esto en lugar de eliminar cuentas."))

    fecha_registro = models.DateTimeField(
        verbose_name=_("fecha de registro"), auto_now_add=True)

    USERNAME_FIELD = 'email'  # Usa el correo electrónico como nombre de usuario único.

    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")
        db_table = 'auth_usuario'

    def get_full_name(self):
        return self.apellidos + "," + self.nombres

    def get_short_name(self):
        return self.nombres

    def has_perm(self, perm, obj=None):
        """EL usuario cuenta con los permisos para ver una app en específico"""
        return True
    
    def __str__(self):
        return self.nombre_usuario + " " + self.email
