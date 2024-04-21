from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants, add_message
from django.contrib import auth


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if senha != confirmar_senha:
            add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 8:
            add_message(request, constants.ERROR, 'A senha deve possuir no minimo 8 caracteres')
            return redirect('/usuarios/cadastro')
        
        users = User.objects.filter(username = username)
        
        if users.exists():
            add_message(request, constants.ERROR, 'O usuario digitado ja existe')
            return redirect('/usuarios/cadastro')


        user = User.objects.create_user(
              username = username,
              email = email,
              password = senha
         )

        return redirect('/usuarios/login')
    
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(request, username = username, password = senha)
        
        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')
        
        add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
        return redirect('/usuarios/login')
    
def logout_view(request):
    auth.logout(request)
    return redirect('/usuarios/login')