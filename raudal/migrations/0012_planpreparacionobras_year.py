# Generated by Django 3.1.4 on 2021-08-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raudal', '0011_auto_20210814_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='planpreparacionobras',
            name='year',
            field=models.PositiveIntegerField(default=None),
        ),
    ]
