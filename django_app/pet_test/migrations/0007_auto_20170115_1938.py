# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_test', '0006_auto_20170115_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importeddata',
            name='PESO',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
