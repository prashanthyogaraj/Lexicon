# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-04 05:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0004_auto_20170704_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standalonetestbedsetup',
            old_name='boot_type',
            new_name='target_type',
        ),
        migrations.RenameField(
            model_name='ucsmtestbedsetup',
            old_name='boot_type',
            new_name='target_type',
        ),
    ]
