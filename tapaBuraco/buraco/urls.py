from django.urls import path
from . import views

urlpatterns = [
	path('', views.paginaInicial, name='paginaInicial'),
	path('receber/', views.get_name, name='receber'),
	path('login/', views.login, name='login'),
	path('buracos/', views.dashburacos, name='buracos'),
	path('agentes/', views.dashagentes, name='agentes'),
]