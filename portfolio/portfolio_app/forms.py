from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}), required=True)
	description = forms.CharField(widget=forms.Textarea, required=True)

	class Meta:
		model = Project
		fields = ['title', 'description']

