from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Portfolio


# Create your views here.
def index(request):
	portfolios = Portfolio.objects.filter(is_active=True)

	# Render index.html
	return render(request, 'portfolio_app/index.html',
			{'portfolios': portfolios})


class PortfolioDetailView(DetailView):
	model = Portfolio
	template_name = 'portfolio_app/portfolio-detail.html'
	context_object_name = 'portfolio'

	def get_context_data(self, **kwargs):
        	context = super().get_context_data(**kwargs)

        	projects = self.object.projects.all()
	        context['projects'] = projects

        	return context


class PortfolioListView(ListView):
	model = Portfolio
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

