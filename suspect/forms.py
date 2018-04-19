from django import forms
from suspect.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class SuspectForm(forms.ModelForm):
    model = Suspect
    exclude = ('created_on')