from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name', 'symptom_notes', 'outbreak', 'created_on', 'modified_on')

    class Meta:
        model = Symptom


admin.site.register(Symptom, SymptomAdmin)