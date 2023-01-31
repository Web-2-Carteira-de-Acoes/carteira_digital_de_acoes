"""cd_acoes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
    
#ana
    path('login', TemplateView.as_view(template_name="layout/formularios/login.html")),
    path('esqueceu_senha', TemplateView.as_view(template_name="layout/formularios/esqueceu_senha.html")),
    path('tela_inicial', TemplateView.as_view(template_name="layout/telas_Iniciais/tela_inicial.html")),
    path('listar_acoes', TemplateView.as_view(template_name="layout/acoes/acoes.html")),
    path('criar_carteira', TemplateView.as_view(template_name="layout/carteiras/criar_carteira.html")),
    path('infos_acoes', TemplateView.as_view(template_name="layout/acoes/informacoes_sobre_as_acoes.html")),
    path('relatorio_geral', TemplateView.as_view(template_name="layout/relatorios/relatorio_geral.html")),
    path('relatorio_especifico_carteira', TemplateView.as_view(template_name="layout/relatorios/relatorios_especificos_carteira.html")),


#samara
    path('telainicial2', TemplateView.as_view(template_name="layout/telas_iniciais/telainicial2.html")),
    path('edicaodacarteira', TemplateView.as_view(template_name="layout/carteiras/edicaodacarteira.html")),
    path('relatorios', TemplateView.as_view(template_name="layout/relatorios/relatorios.html")),
    path('relatoriosespecificos', TemplateView.as_view(template_name="layout/relatorios/relatoriosespecificos.html")),
   # path('cadastro', TemplateView.as_view(template_name="layout/formularios/cadastro.html")),
    path('configuracoesdeusuario', TemplateView.as_view(template_name="layout/config.usuarios/configuracoesdeusuario.html")),

   
   
#icaro
    path('', include('usuarios.urls')),
    path('acoes/', include('acoes.urls')),
    path('carteiras/', include('carteiras.urls')),
    #path('login/', include('usuarios.urls')),



#king

   


 

]
