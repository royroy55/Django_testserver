# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='ftime',
        ),
        migrations.RemoveField(
            model_name='data',
            name='stime',
        ),
        migrations.AddField(
            model_name='data',
            name='datavalue',
            field=models.FloatField(default=0, verbose_name='value'),
        ),
        migrations.AddField(
            model_name='data',
            name='whatdata',
            field=models.CharField(default='DATA', max_length=255, verbose_name='Datatype'),
        ),
    ]
