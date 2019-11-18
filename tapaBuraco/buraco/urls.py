from django.urls import path
from . import views

urlpatterns = [
	path('', views.paginaInicial, name='login'),
	path('painel/', views.dashboard, name='painel'),
]