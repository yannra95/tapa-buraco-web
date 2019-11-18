from django.shortcuts import render

from client.forms import Form

# Create your views here.
def index(request):
	form = Form()
	return render(request, 'client/index.html',  {'form': form})

def sucesso(request):
	return render(request, 'client/sub_sucesso.html')