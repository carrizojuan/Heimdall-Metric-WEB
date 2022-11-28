from django.db import models


class AuthUsuario(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    id = models.UUIDField(primary_key=True)
    nombre_usuario = models.CharField(unique=True, max_length=100)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_usuario'
