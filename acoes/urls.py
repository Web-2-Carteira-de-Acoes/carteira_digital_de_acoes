
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import create_acoe, delete_acoe, list_acoes, update_acoe, buscar_acao

#  Rotas, para a APP de acao

urlpatterns = [
    path('', buscar_acao, name='buscaracao'),
    path('lista', list_acoes, name='listaracoes'),
    path('novo', create_acoe, name='create_acao'),
    path('update/<int:id>/', update_acoe, name='update_acao'),
    path('deletar/<int:id>/', delete_acoe, name='delete_acao'),
    
    
]
