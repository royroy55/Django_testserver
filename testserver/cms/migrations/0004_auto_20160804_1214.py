# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20160804_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='datavalue',
            field=models.FloatField(default=0, verbose_name='value'),
        ),
    ]
