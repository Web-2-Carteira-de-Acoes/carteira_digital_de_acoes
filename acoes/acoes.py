import yfinance as yf
from .codigoAcoes import *
from collections import namedtuple


def traserAcoes(codigo, tipo, pediod):
        
    if(codigo):
        msft = yf.Tickers(codigo)
                
        if(tipo == 'basic_info'):
            return  msft.tickers[codigo].basic_info
        if(tipo == 'history'):
            return  msft.tickers[codigo].history(period=pediod)
        return  msft.tickers[codigo].info
    
    else: 
        msft = yf.Tickers(texto)    
        return  msft.tickers


def acoesFiltradas():
    
    msft = yf.Tickers(texto)
    array = {}
    dados = {}
    
    
    for text in textoArray2:
        codTratado = text.translate(str.maketrans('','','.'))
        acao=msft.tickers[text].fast_info
        dados['nome']=acao.currency 
        dados['preco']=acao.last_price
        array[codTratado] = dados
            #return render(request ,'acoes/teste.html', {'teste' : msft.tickers['BBDC4.SA'].info})

    
    return array


def acoesFiltro(codigo):
    
    msft = yf.Tickers(codigo)
    acao = namedtuple('Acao', ['codigo', 'nome', 'info', 'preco', 'moeda'])
    
    info = msft.tickers[codigo].info
    infoBasic = msft.tickers[codigo].fast_info
    
    dado = acao(codigo.translate(str.maketrans('','','.')), info['longName'], info['longBusinessSummary'],round(infoBasic['last_price'], 2) , infoBasic['currency'])
        #return render(request ,'acoes/teste.html', {'teste' : msft.tickers['BBDC4.SA'].info})
    return dado
