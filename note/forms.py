from django import forms
from .models import notes

class notesupdateform(forms.ModelForm):
  class Meta:
    model = notes
    fields = ['title','notes']
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'notes':forms.Textarea(attrs={'class':'form-control'}),
    }
