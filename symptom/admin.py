from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class SymptomAdmin(admin.ModelAdmin):

    class Meta:
        model = Symptom


admin.site.register(Symptom, SymptomAdmin)