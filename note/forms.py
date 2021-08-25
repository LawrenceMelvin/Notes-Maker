from django import forms
from .models import notes

class notesupdateform(forms.Form):
  class Meta:
    model = notes
    fields = ['title','notes']
