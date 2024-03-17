from django.urls import path
from . import views

from .views import *

urlpatterns = [
	# Define that the empty URL leads to the index view function w/ the tag
	# of "index".
	path('', views.index, name='index'),
	
	path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
	path("", PortfolioListView.as_view(), name="portfolio-list"),
]

