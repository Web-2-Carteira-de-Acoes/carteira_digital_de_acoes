from django.shortcuts import render, redirect
from .models import Acoe
from .forms import AcoesForm
import yfinance as yf
from pprint import pprint
from inspect import getmembers




def list_acoes(request):
    acoes = Acoe.objects.all()
    return render(request, 'list_acoes.html', {'acoes': acoes})


def create_acoe(request):
    form = AcoesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_acoes')

    return render(request, 'acoes-form.html', {'form': form})


def update_acoe(request, id):
    acao = Acoe.objects.get(id=id)
    form = AcoesForm(request.POST or None, instance=acao)

    if form.is_valid():
        form.save()
        return redirect('list_acoes')

    return render(request, 'acoes-form.html', {'form': form, 'acoe': acao})


def delete_acoe(request, id):
    acao = Acoe.objects.get(id=id)

    if request.method == 'POST':
        acao.delete()
        return redirect('list_acoes')

    return render(request, 'acao-delete-confirm.html', {'acao': acao})

def buscar_acao(request):
    teste = yf.Ticker("BBDC4.SA")
    
   
    
    return render(request ,'acoes/teste.html', {'teste': teste.info})
    
    
    