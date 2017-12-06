# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0014_ucsmtestbedsetupfinal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='testbed_stand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.StandaloneTestBedSetupFinal'),
        ),
        migrations.AlterField(
            model_name='testexecution',
            name='testbed_ucsm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.UcsmTestBedSetupFinal'),
        ),
    ]
