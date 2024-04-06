# Author: Jacob Hartt
from django.shortcuts import render
from django.views.generic import DetailView

from .models import *


# Create your views here.
def index(request):
	return render(request, 'goteach_app/index.html')


def classList(request):
	classes = Class.objects.filter(ended=False)

	# Render index.html
	return render(request, 'goteach_app/class_list.html', {'classes': classes})


class ViewClass(DetailView):
	model = Class
	template_name = 'goteach_app/view_class.html'
	context_object_name = 'class'
	pk_url_kwarg = "class_id"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		#classes = self.object.classs.all()
		#context['class_id'] = self.kwargs['class_id']
		
		return context

