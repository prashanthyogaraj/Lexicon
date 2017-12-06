# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0007_remove_standalonetestbedsetup_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestExecution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setup', models.CharField(max_length=100)),
                ('os_bootM', models.CharField(max_length=20)),
                ('os_bootT', models.CharField(max_length=20)),
                ('config', models.CharField(max_length=200)),
                ('pxe_adap', models.CharField(max_length=20)),
                ('cdets', models.CharField(max_length=20)),
                ('auto_logs', models.CharField(max_length=100)),
                ('auto_usage', models.CharField(max_length=10)),
                ('driver_version', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('comments', models.CharField(max_length=500)),
                ('effort', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='standalonetestbedsetup',
            name='effort',
            field=models.CharField(default='N', max_length=10),
        ),
        migrations.AddField(
            model_name='ucsmtestbedsetup',
            name='effort',
            field=models.CharField(default='N', max_length=10),
        ),
        migrations.AlterField(
            model_name='standalonetestbedsetup',
            name='engineer',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='ucsmtestbedsetup',
            name='engineer',
            field=models.CharField(max_length=10),
        ),
    ]