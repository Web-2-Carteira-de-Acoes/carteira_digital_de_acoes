from django.shortcuts import render, redirect
from .models import Carteira
from .forms import CarteiraForm
from carteira_acoes.forms import Carteira_AcoesForm
from acoes.models import Acoes
from acoes.acoes import acoesFiltro
from acoes.views import find_or_create_acao



def list_carteiras(request, usuario_id):
    carteiras = Carteira.objects.get(usuario_id)
    
    if carteiras:
        return render(request, '../templates/layout/carteiras/listar_carteiras.html', {'carteiras': carteiras})
    return render(request, '../templates/layout/carteiras/listar_carteiras.html', {'carteiras': carteiras})




def create_carteira(request):
    
    if request.method == "POST": 
        form = CarteiraForm(request.POST)
        
        if form.is_valid():
            idCarteira = form.save().id
            acoes = Acoes.objects.all
            return render(request, '../templates/layout/carteiras/adicionar_acoes_carteira.html', {'lista':acoes,'carteira': idCarteira})

    return render(request, '../templates/layout/carteiras/criar_carteira.html')


def add_acoes_carteira(request):
    
        
    if request.POST.get('buscaAcao'):
        
        acoes = Acoes.objects.filter(codigo=request.POST.get('buscaAcao')+'SA')
        if acoes:
            
            acoes = Acoes.objects.all
            return render(request, '../templates/layout/carteiras/adicionar_acoes_carteira.html', {'lista': acoes, 'tipo':'busca'})    
        
        dados = acoesFiltro(request.POST.get('buscaAcao')+'.SA')
        find_or_create_acao(dados)
        acoes = Acoes.objects.all            
        return render(request, '../templates/layout/carteiras/adicionar_acoes_carteira.html', {'lista': acoes , 'tipo': 'busca'})
    
    if request.method == "POST":
        acao = []
        dataCompra = []
        quantidadeAtual = []
        precoPago = []
        
        acaoPost = request.POST.getlist('acao')
        datacompraPost = request.POST.getlist('dataCompra')
        quantidade_atualPost = request.POST.getlist('quantidade_atual')
        precoPagoPost =  request.POST.getlist('precoPago')
        
        for ap in acaoPost:
            if ap != '':
                acao.append(ap)
                
        for dt in datacompraPost:
            if dt != '':
                dataCompra.append(dt)
        for qt in quantidade_atualPost:
            if qt != '':
                quantidadeAtual.append(qt)
        for pp in precoPagoPost:
            if pp != '':
                precoPago.append(pp)
            
        for i in range(len(acao)):

            form = Carteira_AcoesForm({'acao': acao[i], 'carteira':  request.POST.get('carteira'), 'quantidade_atual': quantidadeAtual[i],'precoPago': precoPago[i] , 'dataCompra': dataCompra[i]})
            if form.is_valid():
                form.save()
        
        carteiras = Carteira.objects.filter(usuario_id=request.POST.get('usuario_id'))
        
        return render(request, '../templates/layout/carteiras/listar_carteiras.html', {'carteira': carteiras})
        
            
    acoes = Acoes.objects.all
    
    return render(request, '../templates/layout/carteiras/adicionar_acoes_carteira.html', {'lista' : acoes, 'tipo': 'all'})
        
        



def update_carteira(request, id):
    carteira = Carteira.objects.get(id=id)
    form = CarteiraForm(request.POST or None, instance=carteira)

    if form.is_valid():
        form.save()
        return redirect('list_carteiras')

    return render(request, 'carteiras-form.html', {'form': form, 'carteira': carteira})


def delete_carteira(request,id):
    carteira = Carteira.objects.get(id=id)

 
    
   
    carteira.delete()
    carteiras = Carteira.objects.filter(usuario_id=request.POST.get('usuario_id'))
        
    return render(request, '../templates/layout/carteiras/listar_carteiras.html', {'carteira': carteiras})

 