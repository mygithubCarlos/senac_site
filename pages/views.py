from django.shortcuts import render

def home(request):
    contexto = {
        'mensagem': "Seja bem-vindo ao site!"
    }
    return render(request, 'pages/home.html', contexto)

def sobre(request):
    return render(request, "pages/sobre.html")

def contato(request):
    return render(request, "pages/contato.html")

def ajuda(request):
    return render(request, "pages/ajuda.html")

