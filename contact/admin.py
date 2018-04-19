# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nin', 'surname', 'first_name', 'head_of_household', 'phone_number', 'date_of_birth', 'sex',
                    'village_name', 'relation_to_suspect', 'date_of_last_contact', 'status', 'created_on')
    seacrh_field = ['surname ', 'first_name', 'nin']
    list_filter = ('village_name', 'status', 'created_on', 'sex')

    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)


