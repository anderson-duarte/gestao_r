# Generated by Django 3.1.3 on 2020-11-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='hora_extra',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Hora Extra'),
        ),
    ]