from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('auth/login/')
        
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
       username = request.POST.get('username')
       senha = request.POST.get('senha')
       
       user = authenticate(username=username, password=senha)
       
       if user:
           login_django(request, user)
           
           return redirect('/')
       else: 
           return redirect('auth/cadastro/')

@login_required(login_url="/auth/login/")
def logout(request):
    logout_django(request)
    return redirect('auth/login/')
    