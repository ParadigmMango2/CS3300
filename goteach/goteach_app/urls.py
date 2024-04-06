# Author: Jacob Hartt

from django.urls import path
from . import views

from .views import *

urlpatterns = [
	path('', views.index, name='index'),

	path('class_list/', views.classList, name='class_list'),
]

