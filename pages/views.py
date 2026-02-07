from django.shortcuts import render
from django.http import HttpResponse
from pages.forms import ContatoForm

def home(request):
    contexto = {
        'mensagem': "Seja bem-vindo ao site!"
    }
    return render(request, 'pages/home.html', contexto)

def sobre(request):
    return render(request, "pages/sobre.html")

def contato(request):
    if request.method == "GET":
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            return render(
                request,
                'pages/contato_resultado.html',
                {
                    'nome': nome,
                    'email': email
                }
            )
    return render(
        request,
        'pages/contato.html',
        {'form': form}
    )

def ajuda(request):
    return render(request, "pages/ajuda.html")

def saudacao(request, nome, idade):
    return HttpResponse(
        f"<h1>Olá, {nome} de {idade} anos! Bem-vindo(a) ao Site do Senac!</h1>"
    )