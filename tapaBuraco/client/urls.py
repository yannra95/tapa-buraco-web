from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:usuario_id>/enviar/', views.enviar, name='enviar'),
    path('sucesso/', views.sucesso, name='sucesso')
]