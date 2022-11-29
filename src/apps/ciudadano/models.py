from django.db import models


# MODELO IMPORTADO CON INSPECTDB
class AuthUsuario(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    id = models.UUIDField()
    nombre_usuario = models.CharField(unique=True, max_length=100)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    fecha_registro = models.DateTimeField()
    nro_cliente = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'auth_usuario'
