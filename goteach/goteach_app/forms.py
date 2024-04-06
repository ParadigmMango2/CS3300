from django import forms
from .models import *

class ClassForm(forms.ModelForm):
	about = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}), required=True)

	class Meta:
		model = Class
		fields = ['title', 'about', 'ended', 'game_link']

