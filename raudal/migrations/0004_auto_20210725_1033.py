# Generated by Django 3.1.4 on 2021-07-25 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0003_remove_objetoobra_informe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observacion',
            name='objeto_obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='raudal.objetoobra'),
        ),
    ]
