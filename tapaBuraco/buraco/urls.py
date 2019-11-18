from django.urls import path

from . import views

urlpatterns = [
	path('', views.paginaInicial),
	path('receber/', views.get_name),
]