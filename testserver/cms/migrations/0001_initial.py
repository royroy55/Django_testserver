# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stime', models.FloatField(verbose_name='Starttime')),
                ('ftime', models.FloatField(verbose_name='Finishtime')),
            ],
        ),
    ]
