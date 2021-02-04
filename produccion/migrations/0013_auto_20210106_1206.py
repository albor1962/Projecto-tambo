# Generated by Django 3.0 on 2021-01-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_auto_20210106_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingresoalimentos',
            options={'ordering': ['-fecha'], 'verbose_name': 'Ingreso de alimentos', 'verbose_name_plural': 'Ingreso de alimentos'},
        ),
        migrations.AddField(
            model_name='ingresoalimentos',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]