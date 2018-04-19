# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suspect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.CharField(blank=True, max_length=14, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('head_of_household', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(blank=True, max_length=14, null=True)),
                ('village_name', models.CharField(blank=True, max_length=100, null=True)),
                ('relation_to_suspect', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_last_contact', models.DateField()),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('Facility_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField()),
                ('patient_zero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suspect.Suspect')),
            ],
        ),
    ]
