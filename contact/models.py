# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from suspect.models import *

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

class Contact(models.Model):
    nin = models.CharField(max_length=14, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    head_of_household = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=14, blank=True, null=True, choices=SEX)
    village_name = models.CharField(max_length=100, blank=True, null=True)
    relation_to_suspect = models.CharField(max_length=100, blank=True, null=True)
    patient_zero = models.ForeignKey(Suspect)
    date_of_last_contact = models.DateField()
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS)
    Facility_name = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nin

