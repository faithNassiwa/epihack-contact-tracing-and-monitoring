from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class VisitAdmin(admin.ModelAdmin):

    class Meta:
        model = Visit


class DailyFollowUpAdmin(admin.ModelAdmin):

    class Meta:
        model = DailyFollowUp

admin.site.register(Visit, VisitAdmin)
admin.site.register(DailyFollowUp, DailyFollowUpAdmin)

