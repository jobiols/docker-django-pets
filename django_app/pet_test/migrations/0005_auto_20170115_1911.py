# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_test', '0004_auto_20170115_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importeddata',
            name='DETALLE',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
