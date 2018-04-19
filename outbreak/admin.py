from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class OutbreakAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes', 'created_on', 'modified_on')
    filter = ('name', 'created_on')

    class Meta:
        model = Outbreak


admin.site.register(Outbreak, OutbreakAdmin)
