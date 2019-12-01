from django.urls import path
from . import views

urlpatterns = [
	path('', views.paginaInicial, name='paginaInicial'),
	path('receber/', views.get_name, name='receber'),
	path('painel/', views.dashboard, name='painel'),
	path('login/', views.login, name='login')
]