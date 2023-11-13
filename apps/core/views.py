from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.core.forms import LoginForm
import pprint
def DadosPessoaisView(request):		
    return render(request, 'login.html')

def entrar(request):
    form = LoginForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_home')
        else:
            form.add_error(None, 'Nome de usuário ou senha incorretos')
    else:
        print(form.errors)
    return render(request, "login.html", {'form': form})

        
