# Generated by Django 3.1.4 on 2021-08-14 08:34

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0008_remove_informecontratacion_resumengeipi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='resumen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, to='raudal.resumengeipi'),
        ),
    ]
