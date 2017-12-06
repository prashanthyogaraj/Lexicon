# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0016_auto_20170719_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Troubleshooting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setup', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=1000)),
                ('testbed_stand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.StandaloneTestBedSetupFinal')),
                ('testbed_ucsm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Activity.UcsmTestBedSetupFinal')),
            ],
        ),
    ]
