from django.shortcuts import render



def index(request):
    return render(request, 'cadastro/index.html')

def login(request):
    return render(request, 'cadastro/login.html')

def signup(request):
    return render(request, 'cadastro/signup.html')