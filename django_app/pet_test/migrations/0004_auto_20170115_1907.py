# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 22:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_test', '0003_auto_20170115_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importeddata',
            old_name='Código',
            new_name='CODIGO',
        ),
        migrations.RenameField(
            model_name='importeddata',
            old_name='Peso',
            new_name='PESO',
        ),
        migrations.RenameField(
            model_name='importeddata',
            old_name='Precio',
            new_name='PRECIO',
        ),
        migrations.RenameField(
            model_name='importeddata',
            old_name='Stock',
            new_name='STOCK',
        ),
    ]