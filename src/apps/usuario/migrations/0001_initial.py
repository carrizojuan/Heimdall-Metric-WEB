# Generated by Django 3.2 on 2022-10-18 14:05

import apps.usuario.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(help_text='Nombre del Usuario en el sistema', max_length=100, unique=True, verbose_name='nombre usuario')),
                ('nombres', models.CharField(help_text='Nombres de la Persona', max_length=200, verbose_name='nombres')),
                ('apellidos', models.CharField(help_text='Apellidos de la Persona', max_length=200, verbose_name='apellidos')),
                ('email', models.EmailField(error_messages={'unique': 'Un usuario ya está registrado con esta dirección de correo electrónico'}, max_length=254, unique=True, verbose_name='correo electrónico')),
                ('is_staff', models.BooleanField(default=False, help_text='Designa si el usuario puede iniciar sesión en este sitio de administración. True = Administrador False = Monitoreo', verbose_name='staff')),
                ('is_active', models.BooleanField(default=False, help_text='Designa si este usuario debe ser tratado como activo.Anule la selección de esto en lugar de eliminar cuentas.', verbose_name='activo')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'auth_usuario',
            },
            managers=[
                ('objects', apps.usuario.models.UsuarioManager()),
            ],
        ),
    ]