# Generated by Django 3.1.4 on 2021-08-15 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0013_remove_informecontratacion_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='plan',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='raudal.planpreparacionobras'),
        ),
    ]
