from django.shortcuts import render, redirect
from .models import Acoes
from .forms import AcoesForm
import yfinance as yf
from pprint import pprint
from inspect import getmembers
from .acoes import *




def list_acoes(request):
    acoes = Acoes.objects.all()
    return render(request, 'acoes/teste1.html', {'lista': acoes})


def create_acoe(request):
    form = AcoesForm(request.POST or None)

    if form.is_valid():
        form.save()
        print(request)
        return redirect('list_acoes')

    return render(request, 'acoes-form.html', {'form': form})


def update_acoe(request, id):
    acao = Acoes.objects.get(id=id)
    form = AcoesForm(request.POST or None, instance=acao)

    if form.is_valid():
        form.save()
        return redirect('list_acoes')

    return render(request, 'acoes-form.html', {'form': form, 'acoe': acao})


def delete_acoe(request, id):
    acao = Acoes.objects.get(id=id)

    if request.method == 'POST':
        acao.delete()
        return redirect('list_acoes')

    return render(request, 'acao-delete-confirm.html', {'acao': acao})




def buscar_acao(request):
    #tickers = yf.Tickers('msft, aapl, goog, ITSA4.SA, BBDC4.SA')
    #tickers = yf.Tickers('aapl')
    texto = "MSFT BBDC4.SA"
    msft = yf.Tickers(texto)

    form = AcoesForm()
    
    
   # if request.method == "GET":
    
    teste = traserAcoes(False,False,False)
    teste2 = acoesFiltradas()
    
     

    return render(request ,'acoes/teste.html', {'teste' : teste2 })
    #return render(request ,'acoes/teste.html', {'teste' : msft.tickers['BBDC4.SA'].info})
    #return render(request ,'acoes/teste.html', {'teste' : msft.tickers})

    #else:
    #    form = AcoesForm(request.POST)
     #   if form.is_valid():
     #       acao = form.save()
     #       form = AcoesForm()
            
      #  else:
      #      return render(request ,'acoes/teste.html', {'teste': 'deu ruim'})