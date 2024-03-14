from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Portfolio


# Create your views here.
def index(request):
	portfolios = Portfolio.objects.filter(is_active=True)

	# Render index.html
	return render(request, 'portfolio_app/index.html',
			{'portfolios': portfolios})


class PortfolioListView(ListView):
	model = Portfolio
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

