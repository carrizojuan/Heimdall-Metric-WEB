# Generated by Django 3.2 on 2022-12-20 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('correo', '0002_emailservice_id_entidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailservice',
            old_name='id_entidad',
            new_name='entidad',
        ),
    ]