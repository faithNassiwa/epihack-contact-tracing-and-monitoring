# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEX = (
    ('male', 'Male'),
    ('female', 'Female')

)

STATUS = (
    ('admitted', 'Admitted'),
    ('discharged', 'Discharged'),
    ('loss to follow up ', 'Loss to follow up '),
    ('dead', 'Dead')

)

class Suspect(models.Model):
    case_id = models.CharField(max_length=14, blank=True, null=True)
    nin = models.CharField(max_length=14, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    head_of_household = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=14, blank=True, null=True, choices=SEX)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(default=0.347596)
    longitude = models.FloatField(default=32.582520)
    date_of_onset = models.DateField()
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nin


