# Generated by Django 3.0 on 2021-01-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_proleche'),
    ]

    operations = [
        migrations.AddField(
            model_name='proleche',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
