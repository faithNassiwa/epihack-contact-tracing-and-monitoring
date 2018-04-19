# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from outbreak.models import Outbreak

# Create your models here.

class Symptom(models.Model):
    name= models.CharField(max_length=14, blank=True, null=True)
    symptom_notes = models.CharField(max_length=14, blank=True, null=True)
    outbreak = models.ForeignKey(Outbreak, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
