from django.http import HttpResponseRedirect
from django.shortcuts import render
from buraco.forms import *
from buraco.models import *

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("Formulário válido!")
            # process the data in form.cleaned_data as required
            # 
            print(form.cleaned_data)
            latitude=form.cleaned_data['latitude']
            longitude=form.cleaned_data['longitude']
            acc=form.cleaned_data['acc']
            cidadao=Cidadao.objects.get(id=form.cleaned_data['usuario_id'])
            buraco = Buraco(
                latitude = latitude,
                longitude = longitude,
                acc = acc)
            buraco.save()
            buraco.cidadao.set(cidadao)

            # redirect to a new URL:
            return HttpResponseRedirect('/client/sucesso')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Form()

    return render(request, 'client/index.html')

def login(request):

    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():

            email_input = loginForm.cleaned_data['email']
            senha_input = loginForm.cleaned_data['senha']
            agente = None
            cidadao = None

            try:
                usuario = Usuario.objects.get(email=email_input, senha=senha_input)
                try:
                    agente = Agente.objects.get(userid=usuario)
                    print('-----Agente:', agente.name)
                except Exception as e:
                    pass
                try:
                    cidadao = Cidadao.objects.get(userid=usuario)
                    print('-----Cidadao:', cidadao.name, "id:", cidadao.id)
                except Exception as e:
                    pass

                if agente != None:
                    return HttpResponseRedirect('/buracos')
                else:
                    return HttpResponseRedirect('/client/'+str(cidadao.id)+'/enviar')
            except Usuario.DoesNotExist:
                print("Usuário não encontrado")
                return render(request, 'login_fail.html')
            # except Usuario.MultipleObjectsReturned:
                # what to do if multiple employees have been returned? 
        else:
            print("----------- Formulario invalido")

    return render(request, 'login.html')

# Create your views here.
def paginaInicial(request):
    loginForm = LoginForm()
    return render(request, 'login.html', {'loginForm': loginForm})

def dashburacos(request):
    return render(request, "dash_buracos.html")

def dashagentes(request):
    return render(request, "dash_agentes.html")
