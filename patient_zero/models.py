# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class patient_zero(models.Model):
    nin = models.CharField(max_length=14, blank=True, null=True)
