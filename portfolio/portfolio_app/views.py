from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# Rigidly returns an http response with unformatted text.
	return HttpResponse('home page')

