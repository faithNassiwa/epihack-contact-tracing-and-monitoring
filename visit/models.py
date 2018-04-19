# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from suspect.models import *
from contact.models import *
from symptom.models import *
# Create your models here.

SYMPTOM_STATUS = (
    ('yes', 'Yes'),
    ('no', 'No')

)

class Visit(models.Model):
    date = models.DateField(blank=True, null=True)
    suspect = models.ForeignKey(Suspect, blank=True, null=True)
    contact = models.ForeignKey(Contact, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    Temperature = models.IntegerField(blank=True, null=True)
    lab_sample = models.CharField(max_length=20, blank=True, null=True)
    lab_sample_id = models.CharField(max_length=20, blank=True, null=True)
    next_appointment_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class DailyFollowUp(models.Model):
    symptoms = models.ForeignKey(Symptom, blank=True, null=True)
    symptom_status = models.CharField(max_length=20, blank=True, null=True, choices=SYMPTOM_STATUS )
    visit = models.ForeignKey(Visit, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)



