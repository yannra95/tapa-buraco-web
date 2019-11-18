from django.shortcuts import render, HttpResponse

# Create your views here.
def paginaInicial(request):
	descricao = "Uma desc dinamica"
	return render(request, "index.html", {"des":descricao})

def dashboard(request):
	return render(request, "dashboard.html")

