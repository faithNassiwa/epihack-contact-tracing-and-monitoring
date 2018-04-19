# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suspect', '0002_suspect_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspect',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
