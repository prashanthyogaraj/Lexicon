# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0005_auto_20170704_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='standalonetestbedsetup',
            name='engineer',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='ucsmtestbedsetup',
            name='engineer',
            field=models.CharField(default='NA', max_length=10),
        ),
    ]
