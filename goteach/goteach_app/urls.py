# Author: Jacob Hartt

from django.urls import path
from . import views

from .views import *

urlpatterns = [
	path('', views.index, name='index'),

	path('classes/', views.classList, name='class_list'),
	path('classes/<int:class_id>/', ViewClass.as_view(), name='view_class'),
	path('classes/<int:class_id>/update_class/', views.updateClass, name='update_class'), 
	path('classes/create_class/', views.createClass, name='create_class'),
]

