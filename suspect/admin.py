# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class SuspectAdmin(admin.ModelAdmin):
    list_display = ('nin', 'surname', 'first_name', 'head_of_household', 'phone_number', 'date_of_birth', 'sex',
                    'village_name', 'date_of_onset', 'status', 'created_on')
    seacrh_field = ['surname ', 'first_name', 'nin']

    class Meta:
        model = Suspect


admin.site.register(Suspect, SuspectAdmin)
