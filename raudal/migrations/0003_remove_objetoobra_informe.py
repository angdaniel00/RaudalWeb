# Generated by Django 3.1.4 on 2021-07-25 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0002_auto_20210725_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objetoobra',
            name='informe',
        ),
    ]
