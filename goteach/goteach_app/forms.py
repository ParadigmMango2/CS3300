from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class ClassForm(forms.ModelForm):
	about = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}), required=False)
	start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

	class Meta:
		model = Class
		fields = ['title', 'start_date', 'about', 'ended', 'game_link', 'presentation_file']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'groups']
