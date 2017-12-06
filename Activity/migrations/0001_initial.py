# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UcsmAddAcivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(max_length=200)),
                ('Config', models.CharField(max_length=999)),
                ('Fidetails', models.CharField(max_length=50)),
                ('fiFirmware', models.CharField(max_length=50)),
                ('ucsmBuild', models.CharField(max_length=50)),
                ('cimc', models.CharField(max_length=50)),
                ('bios', models.CharField(max_length=50)),
                ('adapters', models.CharField(max_length=500)),
                ('slot', models.CharField(max_length=50)),
                ('adapterFirmware', models.CharField(max_length=250)),
                ('boot', models.CharField(max_length=50)),
                ('adapterBios', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('driver', models.CharField(max_length=999)),
                ('automationUsage', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
                ('bigzillaId', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=2000)),
                ('remarks', models.CharField(max_length=2000)),
            ],
        ),
    ]
