# Author: Jacob Hartt
from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
	return render(request, 'goteach_app/index.html')


def classList(request):
	classes = Class.objects.filter(ended=False)

	# Render index.html
	return render(request, 'goteach_app/class_list.html', {'classes': classes})

