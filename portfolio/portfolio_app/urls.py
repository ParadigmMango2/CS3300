from django.urls import path
from . import views

from .views import *

urlpatterns = [
	# Define that the empty URL leads to the index view function w/ the tag
	# of "index".
	path('', views.index, name='index'),

	path('student/', views.studentList, name='student_list'),
	path('student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
	
	path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'), 
	path('portfolio/<int:portfolio_id>/update_project/<int:project_id>/', views.updateProject, name='update_project'), 
	path('portfolio/<int:portfolio_id>/delete_project/<int:project_id>/', views.deleteProject, name='delete_project'), 
	path('portfolio/<int:portfolio_id>/view_project/<int:project_id>/', ProjectDetailView.as_view(), name='view_project'),

	path('portfolio/<int:portfolio_id>/update_portfolio/', views.updatePortfolio, name='update_portfolio'), 
	path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),

	path('', PortfolioListView.as_view(), name='portfolio_list'),
]

