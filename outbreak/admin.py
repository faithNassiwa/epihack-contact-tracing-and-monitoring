from __future__ import unicode_literals

from django.contrib import admin
from suspect.models import *
from models import *
# Register your models here.

class OutbreakAdmin(admin.ModelAdmin):

    class Meta:
        model = Outbreak


admin.site.register(Outbreak, OutbreakAdmin)
