# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2010-06-30 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0019_ucsmtestbedsetupfinal_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='standalonetestbedsetup',
            name='release',
            field=models.CharField(default='na', max_length=50),
        ),
        migrations.AddField(
            model_name='standalonetestbedsetupfinal',
            name='release',
            field=models.CharField(default='na', max_length=50),
        ),
        migrations.AddField(
            model_name='ucsmtestbedsetup',
            name='release',
            field=models.CharField(default='na', max_length=50),
        ),
        migrations.AddField(
            model_name='ucsmtestbedsetupfinal',
            name='release',
            field=models.CharField(default='na', max_length=50),
        ),
    ]