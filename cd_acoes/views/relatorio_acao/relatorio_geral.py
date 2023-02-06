from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import plotly.graph_objects as go
import yfinance as yf


def index(request):
    # return render(request, 'indexTest.html')

    return TemplateView.as_view(template_name="index.html")


def relatorio_geral(request):
    # return render(request, 'indexTest.html')

    nome_da_acao = "LMT"
    nome_da_acao = "^BVSP"

    menssagem = "Relatório Geral: " + nome_da_acao
    
    acao = yf.Ticker(nome_da_acao)

    dados1 = acao.history(period="1mo")
    dados1 = dados1.sort_values('Date')
    Close = dados1['Close']
    Open = dados1['Open']
    High = dados1['High']
    # dados1.columns = ['Coluna_1', 'Coluna_2']
    # dados1.drop(2)
    print(dados1)
    figura = go.Figure()

    # figura.add_bar(
    #     x=['2010', '2011', '2012', '2013', '2014', '2015',
    #         '2016', '2017', '2018', '2019', '2020', '2021'],
    #     y=[4626094, 5380857,  5791332, 7173574,
    #         8722290, 7792025,  8627371,	6731186,
    #         5513662, 5095308, 5783357, 4004764
    #         ],
    #     name='num de inscritos')

    figura.add_scatter(
        x=Close.index,
        y=Close,
        name='Fechamento'
        )

    figura.add_scatter(
        x=Open.index,
        y=Open,
        name='Abertura'
        )

    figura.add_box(
        x=High.index,
        y=High,
        name='Maior valor'
        )

    figura.update_layout(
        title_text='Valor da ação por semana.',
        height=400,
        xaxis_title="Ano",
        yaxis_title="valor em Moeda em USD",
        legend_title="Legenda",
        font=dict(
            family="Arial",
            size=12,
            color="black"
        )
    )

    relatorio = figura.to_html()
    dados = dados1.to_html()

    context = {
        'dados': dados,
        'menssagem': menssagem,
        'relatorio': relatorio
    }

    if request.method == 'GET':
        return render(request, 'layout/relatorios/relatorio_geral.html', context=context)
    else:
        return render(request, 'layout/relatorios/relatorio_geral.html', context=context)
    # return TemplateView.as_view(template_name="dashboard.html")
