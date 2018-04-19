# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0002_auto_20180419_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='symptom',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
