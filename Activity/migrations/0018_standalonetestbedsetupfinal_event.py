# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0017_troubleshooting'),
    ]

    operations = [
        migrations.AddField(
            model_name='standalonetestbedsetupfinal',
            name='event',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
