from django import forms
from .models import notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class notesupdate(forms.ModelForm):
  class Meta:
    model = notes
    fields = ['title','notes']
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'notes':forms.Textarea(attrs={'class':'form-control'}),
    }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user