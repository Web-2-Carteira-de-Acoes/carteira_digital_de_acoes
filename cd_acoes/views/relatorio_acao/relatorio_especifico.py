from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

def index(request):
    # return render(request, 'indexTest.html')
    
    return TemplateView.as_view(template_name="index.html")


def relatorio_especifico(request):
    # return render(request, 'indexTest.html')
    
    menssagem = """Carteira X"""

    context = {
        'menssagem': menssagem
    }

    if request.method == 'GET':
        return render(request, 'layout/relatorios/relatorios_especificos_carteira.html', context=context)
    else:
        return render(request, 'layout/relatorios/relatorios_especificos_carteira.html')
    # return TemplateView.as_view(template_name="dashboard.html")
