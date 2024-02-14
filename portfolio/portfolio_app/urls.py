from django.urls import path
from . import views

urlpatterns = [
	# Define that the empty URL leads to the index view function w/ the tag
	# of "index".
	path('', views.index, name='index'),
]

