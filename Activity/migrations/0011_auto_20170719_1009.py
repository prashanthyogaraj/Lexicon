# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0010_auto_20170719_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testexecution',
            name='testbed',
            field=models.IntegerField(default='NA', editable=False, primary_key=True, serialize=False),
        ),
    ]
