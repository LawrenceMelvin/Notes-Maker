from django import forms
from .models import notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class notesupdateform(forms.ModelForm):
  class Meta:
    model = notes
    fields = ['title','notes']
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'notes':forms.Textarea(attrs={'class':'form-control'}),
    }

class createuserform(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    widgets = {
      'username':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.TextInput(attrs={'class':'form-control'}),
    }
