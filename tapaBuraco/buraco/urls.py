from django.urls import path
from . import views

urlpatterns = [
	path('', views.paginaInicial, name='login'),
	path('receber/', views.get_name, name='receber'),
	path('painel/', views.dashboard, name='painel'),
]