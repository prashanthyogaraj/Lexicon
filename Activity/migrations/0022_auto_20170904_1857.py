# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-04 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0021_testexecution_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='testbed_stand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.StandaloneTestBedSetupFinal'),
        ),
        migrations.AlterField(
            model_name='testexecution',
            name='testbed_ucsm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.UcsmTestBedSetupFinal'),
        ),
    ]
