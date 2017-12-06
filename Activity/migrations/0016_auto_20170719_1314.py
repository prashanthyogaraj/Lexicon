# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0015_auto_20170719_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='standalonetestbedsetup',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standalonetestbedsetupfinal',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='standalonetestbedsetup',
            name='effort',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='standalonetestbedsetupfinal',
            name='effort',
            field=models.CharField(max_length=10),
        ),
    ]
