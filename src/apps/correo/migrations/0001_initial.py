# Generated by Django 3.2 on 2022-12-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('port', models.PositiveSmallIntegerField()),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('use_tls', models.BooleanField()),
            ],
        ),
    ]
