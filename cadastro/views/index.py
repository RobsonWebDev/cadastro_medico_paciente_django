from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_dj



def index(request):
    if request.user.is_authenticated:
        return render(request, 'cadastro/index.html')
    
    return render(request, 'cadastro/login.html')

def login(request):
    if request.method == "GET":
        return render(request, 'cadastro/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, username=email, password=senha)

        if user:
            login_dj(request, user)
            return render(request, 'cadastro/index.html')
        else:
            return HttpResponse('email ou senha invalido')

def signup(request):
    if request.method == "GET":
        return render(request, 'cadastro/signup.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user_checked = User.objects.filter(email=email)

        if user_checked:
            return HttpResponse("usuario ja cadastrado")
        
        user = User.objects.create_user(username=email, first_name=nome, last_name=sobrenome, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado com sucesso')
