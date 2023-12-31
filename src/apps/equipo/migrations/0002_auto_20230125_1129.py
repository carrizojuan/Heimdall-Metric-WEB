# Generated by Django 3.2 on 2023-01-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='latitud',
            field=models.DecimalField(decimal_places=17, help_text='latitud', max_digits=20, null=True, verbose_name='latitud'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='longitud',
            field=models.DecimalField(decimal_places=17, help_text='longitud', max_digits=20, null=True, verbose_name='longitud'),
        ),
    ]
