from django.shortcuts import render

from buraco.forms import *

def index(request):
    loginForm = LoginForm()
    return render(request, 'client/login.html', {'loginForm': loginForm})

def enviar(request, usuario_id):
	form = Form()
	print("--------------- ID do usuário", usuario_id)
	return render(request, 'client/enviar.html', {'form': form, 'usuario_id': usuario_id})

def sucesso(request):
	return render(request, 'client/sub_sucesso.html')