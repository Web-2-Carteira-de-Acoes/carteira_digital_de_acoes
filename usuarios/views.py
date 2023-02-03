# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#from django.contrib import admin
from .forms import UserForm

# Create your views here.

def home(request):
    template_name = '../templates/layout/formularios/cadastro.html'
    data = {}
    if request.method == 'POST':
        if (request.POST['name']==""):
            data['msg'] = 'digite um Nome'
            data['class'] = 'alert-danger'
            return render(request,'../templates/layout/formularios/cadastro.html',data)
        elif (request.POST['user']==""):
            data['msg'] = 'digite um username'
            data['class'] = 'alert-danger'
            return render(request,'../templates/layout/formularios/cadastro.html',data)
        elif (request.POST['email']==""):
            data['msg'] = 'digite um email'
            data['class'] = 'alert-danger'
            return render(request,'../templates/layout/formularios/cadastro.html',data)
        elif (request.POST['password-conf']==""):
            data['msg'] = 'digite uma senha'
            data['class'] = 'alert-danger'
            return render(request,'../templates/layout/formularios/cadastro.html',data)
        else:
            user = User.objects.create_user(request.POST['user'],
                                            first_name=request.POST['name'],
                                            email=request.POST['email'],
                                            password=request.POST['password']
                                            )
            user.last_name = request.POST['user']
            user.save()
            data['msg'] = 'usuario cadastrado'
            data['class'] = 'alert alert-success'
            return render(request,'../templates/layout/formularios/cadastro.html',data)
    else:
        return render(request, template_name, data)

##############################################################

def user_login(request):
    template_name = '../templates/layout/formularios/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            data = {}
            data['msg'] = 'digite uma usuario valido'
            data['class'] = 'alert-danger'
            return render(request,template_name,data)

    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_profile(request):
    template_name = '../templates/dashboard.html'
    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    # return redirect('accounts:home')
    return redirect('/login')
