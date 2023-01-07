from django.shortcuts import render, redirect
from .models import Acoes
from .forms import AcoesForm
import yfinance as yf
from pprint import pprint
from inspect import getmembers




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
    tickers = yf.Tickers('msft, aapl, goog, ITSA4.SA, BBDC4.SA')

    form = AcoesForm()
    
    
    if request.method == "GET":
    
    
        #return render(request ,'acoes/teste.html', {'teste': tickers.tickers.AAPL})
        return render(request ,'acoes/teste.html', {'teste': tickers.tickers['ITSA4.SA'].info})

    else:
        form = AcoesForm(request.POST)
        if form.is_valid():
            acao = form.save()
            form = AcoesForm()
            
        else:
            return render(request ,'acoes/teste.html', {'teste': 'deu ruim'})