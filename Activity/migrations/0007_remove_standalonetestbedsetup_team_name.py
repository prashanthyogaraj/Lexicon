# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 05:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0006_auto_20170713_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standalonetestbedsetup',
            name='team_name',
        ),
    ]
