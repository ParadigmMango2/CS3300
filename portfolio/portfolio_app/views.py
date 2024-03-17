from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Portfolio, Project
from .forms import *


# Create your views here.
def index(request):
	portfolios = Portfolio.objects.filter(is_active=True)

	# Render index.html
	return render(request, 'portfolio_app/index.html',
			{'portfolios': portfolios})


class PortfolioDetailView(DetailView):
	model = Portfolio
	template_name = 'portfolio_app/portfolio_detail.html'
	context_object_name = 'portfolio'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		projects = self.object.projects.all()
		context['projects'] = projects
		context['portfolio_id'] = self.kwargs['pk']
		
		return context


def createProject(request, portfolio_id):
	form = ProjectForm()
	
	if request.method == 'POST':
		if 'save' in request.POST:
			form = ProjectForm(request.POST)
			project = form.save(commit=False)
			project.portfolio = Portfolio.objects.get(pk=portfolio_id)
			
			project.save()
			
			return redirect('portfolio_detail', pk=portfolio_id)

	context = {}
	context['portfolio_id'] = portfolio_id
	context['form'] = form

	return render(request, 'portfolio_app/create_project.html', context)	


class ProjectDetailView(DetailView):
	model = Project
	template_name = 'portfolio_app/view_project.html'
	context_object_name = 'project'

	def get_object(self, queryset=None):
		project_id = self.kwargs.get('project_id')
		return Project.objects.filter(id=project_id).first()

	def get_context_data(self, **kwargs):
        	context = super().get_context_data(**kwargs)
        	return context


class PortfolioListView(ListView):
	model = Portfolio
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

