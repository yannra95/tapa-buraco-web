from django.http import HttpResponseRedirect
from django.shortcuts import render
from client.forms import Form

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            print(form.cleaned_data)

            # redirect to a new URL:
            return HttpResponseRedirect('/client/sucesso')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Form()

    return render(request, 'client/index.html')


# Create your views here.
def paginaInicial(request):
	# descricao = 'Uma desc dinamica'
	# return render(request, 'buraco/index.html', {'desc': descricao})
	return render(request, 'buraco/index.html')

def dashboard(request):
    return render(request, "dashboard.html")

