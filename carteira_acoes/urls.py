
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import add_acoes_carteira

#  Rotas, para a APP de Carteira

urlpatterns = [
    path('adicionar_acoes_carteira', add_acoes_carteira, name='add_acoes_carteira') 
]

