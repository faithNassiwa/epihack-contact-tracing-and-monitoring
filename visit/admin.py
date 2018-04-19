from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'suspect', 'contact', 'height', 'weight', 'Temperature','lab_sample' ,'lab_sample_id',
                    'next_appointment_date', 'created_on', 'modified_on')
    list_filter = ('created_on', 'modified_on', 'lab_sample', 'next_appointment_date')

    class Meta:
        model = Visit


class DailyFollowUpAdmin(admin.ModelAdmin):
    list_display = ('symptom', 'symptom_status', 'visit', 'created_on', 'modified_on')
    list_filter = ('created_on', 'modified_on', 'symptom')

    class Meta:
        model = DailyFollowUp

admin.site.register(Visit, VisitAdmin)
admin.site.register(DailyFollowUp, DailyFollowUpAdmin)

