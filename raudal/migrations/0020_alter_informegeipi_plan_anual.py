# Generated by Django 3.2.7 on 2021-10-19 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0019_suplemento_valor_actual_contratado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informegeipi',
            name='plan_anual',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
