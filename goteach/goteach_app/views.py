# Author: Jacob Hartt
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.forms.models import model_to_dict
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib.auth import logout

from .models import *
from .forms import *


# Helper functions
def upload_file(file):   
	file_path = settings.MEDIA_ROOT + "/presentations/" + file.name

	with default_storage.open(file_path, 'wb+') as destination:   
		for chunk in file.chunks(): 
			destination.write(chunk)   

	return file_path


# Logout
def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


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

		class_obj = self.get_object()
		presentation_file = class_obj.presentation_file 
	
		if presentation_file:
			context['rel_presentation_path'] = presentation_file.path.removeprefix(str(settings.BASE_DIR))
		else:
			context['rel_presentation_path'] = None

		print(settings.MEDIA_ROOT)
		print(settings.STATIC_ROOT)
		print(settings.BASE_DIR)
		print(context['rel_presentation_path'])

		#classes = self.object.classs.all()
		#context['class_id'] = self.kwargs['class_id']
		
		return context


def updateClass(request, class_id):
	class_obj = Class.objects.get(id=class_id)
	form = ClassForm(initial=model_to_dict(class_obj), instance=class_obj)
	
	if request.method == 'POST':
		form = ClassForm(request.POST, request.FILES, instance=class_obj)
		
		class_obj = form.save(commit=False)

		if 'presentation_file' in request.FILES:
			uploaded_file = request.FILES['presentation_file']
			file_path = upload_file(uploaded_file)
			class_obj.presentation_file = file_path

		class_obj.save()

		return redirect('view_class', class_id=class_id)

	context = {}
	context['class'] = class_obj
	context['form'] = form

	return render(request, 'goteach_app/update_class.html', context)	


def createClass(request):
	form = ClassForm()
	
	if request.method == 'POST':
		if 'save' in request.POST:
			form = ClassForm(request.POST, request.FILES)

			class_obj = form.save(commit=False)

			if 'presentation_file' in request.FILES:
				uploaded_file = request.FILES['presentation_file']
				file_path = upload_file(uploaded_file)
				class_obj.presentation_file = file_path

			class_obj.save()
			
			return redirect('class_list')

	context = {}
	context['form'] = form

	return render(request, 'goteach_app/create_class.html', context)	


def deleteClass(request, class_id):
	class_obj = Class.objects.get(id=class_id)
	
	if request.method == 'POST':
		if 'delete' in request.POST:
			class_obj.delete()

		return redirect('class_list')

	context = {}
	context['class'] = class_obj

	return render(request, 'goteach_app/delete_class.html', context)	

