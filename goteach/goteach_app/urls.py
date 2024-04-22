# Author: Jacob Hartt

from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from . import views

from .views import *

urlpatterns = [
	# Basic URLs
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),

	# Account URLs
	path('accounts/logout/', views.custom_logout, name='logoutView'),
	path('accounts/register/', views.register, name='registerView'),
	path('accounts/', include('django.contrib.auth.urls')),

	# Class object URLs
	path('classes/', views.classList, name='class_list'),
	path('classes/<int:class_id>/', ViewClass.as_view(), name='view_class'),
	# path('classes/<int:class_id>/update_class/', views.updateClass, name='update_class'), 
	path('classes/<int:class_id>/update_class/', UpdateClassView.as_view(), name='update_class'), 
	# path('classes/create_class/', views.createClass, name='create_class'),
	path('classes/create_class/', CreateClassView.as_view(), name='create_class'),
	# path('classes/<int:class_id>/delete_class/', views.deleteClass, name='delete_class'), 
	path('classes/<int:class_id>/delete_class/', DeleteClassView.as_view(), name='delete_class'), 
 ]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
