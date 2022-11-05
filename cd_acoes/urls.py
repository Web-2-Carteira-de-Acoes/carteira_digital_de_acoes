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
    path('', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
 

    path('Login', TemplateView.as_view(template_name="acoes/login.html")),
    path('Tela_Inicial', TemplateView.as_view(template_name="acoes/tela_inicial.html")),
    path('Criar_Carteira', TemplateView.as_view(template_name="acoes/criar_carteira.html")),
    path('Infos_Acoes', TemplateView.as_view(template_name="acoes/informacoes_sobre_as_acoes.html")),
    path('Relatorio_Geral', TemplateView.as_view(template_name="acoes/relatorio_geral.html")),
    path('Relatorio_Especifico_Carteira', TemplateView.as_view(template_name="acoes/relatorios_especificos_carteira.html")),
    
    path('cadastro', TemplateView.as_view(template_name="acoes/cadastro.html")),
    path('Listar_Acoes', TemplateView.as_view(template_name="acoes/acoes.html")),
    path('configuracoesdeusuario', TemplateView.as_view(template_name="acoes/configuracoesdeusuario.html")),
    path('telainicial2', TemplateView.as_view(template_name="acoes/telainicial2.html")),

    path('edicaodacarteira', TemplateView.as_view(template_name="acoes/edicaodacarteira.html")),
    path('relatorios', TemplateView.as_view(template_name="acoes/relatorios.html")),
    path('relatoriosespecificos', TemplateView.as_view(template_name="acoes/relatoriosespecificos.html")),
   
    path('login/', include('usuarios.urls')),

    path('usuarios/', include('usuarios.urls')),
    path('acoes/', include('acoes.urls')),
    path('carteiras/', include('carteiras.urls'))

 


]

