from django.shortcuts import render

def home(request):
    contexto = {
        'mensagem': "Seja bem-vindo ao site!"
    }
    return render(request, 'pages/home.html', contexto)

