from django.shortcuts import render, redirect
from .models import Acoes
from .forms import AcoesForm
import yfinance as yf
from pprint import pprint
from inspect import getmembers
from .acoes import *




def list_acoes(request):
   
    if request.method == "POST":
        
        acoes = Acoes.objects.filter(codigo=request.POST.get('codigoAcao')+'SA')
        if acoes:
            
            return render(request, '../templates/layout/acoes/acoes.html', {'lista': acoes[0], 'tipo':'busca'})    
        
        dados = acoesFiltro(request.POST.get('codigoAcao')+'.SA')
        find_or_create_acao(dados)            
        return render(request, '../templates/layout/acoes/acoes.html', {'lista': dados , 'tipo': 'busca'})
            
    acoes = Acoes.objects.all
    
    return render(request, '../templates/layout/acoes/acoes.html', {'lista' : acoes, 'tipo': 'all'})


def create_acoe(request):
    
    form = AcoesForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_acoes', {'form': form})
    else:
        return render(request, 'acoes-form.html', {'form': 'Deu erro, não inseriu'})


def find_or_create_acao(dados):
    
    #form = AcoesForm({  'nome': '2dasdadasd', 'preco':'20.4', 'info': 'tesasdasdasdaste', 'codigo': 'https://shopee.com.b', 'moeda': 'venezu22222222éla'})
    form = AcoesForm({'nome': dados.nome , 'preco': dados.preco, 'info': dados.info, 'codigo': dados.codigo, 'moeda': dados.moeda})
    if form.is_valid():
        form.save()

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



