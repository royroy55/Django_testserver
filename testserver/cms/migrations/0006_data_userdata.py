# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-24 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20160804_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='userdata',
            field=models.CharField(default='NAME', max_length=255, verbose_name='username'),
        ),
    ]