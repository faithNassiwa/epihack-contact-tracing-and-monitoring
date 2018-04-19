# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suspect', '0004_auto_20180419_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspect',
            name='latitude',
            field=models.FloatField(default=0.347596),
        ),
        migrations.AddField(
            model_name='suspect',
            name='longitude',
            field=models.FloatField(default=32.58252),
        ),
    ]
