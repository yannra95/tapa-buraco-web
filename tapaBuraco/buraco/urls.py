from django.urls import path
from . import views

urlpatterns = [
	path('', views.paginaInicial, name='login'),
	path('receber/', views.get_name, name='receber'),
	path('buracos/', views.dashburacos, name='buracos'),
	path('agentes/', views.dashagentes, name='agentes'),
]