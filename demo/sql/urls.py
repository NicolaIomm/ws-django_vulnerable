from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('init', views.init, name='init'),
	path('reset', views.reset, name='reset'),
]