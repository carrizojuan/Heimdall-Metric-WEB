# Generated by Django 3.2 on 2022-11-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipo_gateway', '0002_consola'),
    ]

    operations = [
        migrations.AddField(
            model_name='consola',
            name='nombre',
            field=models.CharField(help_text='Nombre de la consola', max_length=255, null=True, verbose_name='nombre'),
        ),
    ]