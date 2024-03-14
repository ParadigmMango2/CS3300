from django.urls import path
from . import views

from .views import PortfolioListView

urlpatterns = [
	# Define that the empty URL leads to the index view function w/ the tag
	# of "index".
	path('', views.index, name='index'),
	
	path("", PortfolioListView.as_view(), name="portfolio-list"),
]

