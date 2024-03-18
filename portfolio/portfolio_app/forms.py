from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
	description = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}), required=True)

	class Meta:
		model = Project
		fields = ['title', 'description']


class PortfolioForm(forms.ModelForm):
	about = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 20}), required=False)

	class Meta:
		model = Portfolio
		fields = ['title', 'about', 'is_active', 'contact_email']

