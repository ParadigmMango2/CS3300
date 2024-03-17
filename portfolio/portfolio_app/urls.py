from django.urls import path
from . import views

from .views import *

urlpatterns = [
	# Define that the empty URL leads to the index view function w/ the tag
	# of "index".
	path('', views.index, name='index'),
	
	path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'), 
	path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
	path('portfolio/<int:portfolio_id>/view_project/<int:project_id>/', ProjectDetailView.as_view(), name='view_project'),
	path('', PortfolioListView.as_view(), name='portfolio-list'),
]

