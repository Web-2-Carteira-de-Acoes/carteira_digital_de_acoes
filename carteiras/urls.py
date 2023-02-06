
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import create_carteira, add_acoes_carteira , delete_carteira, list_carteiras, update_carteira, list_acoes_carteira

#  Rotas, para a APP de Carteira

urlpatterns = [
    path('', list_carteiras, name='list_carteiras'),
    path('novo', create_carteira, name='create_carteira'),
    path('novo/acoes', add_acoes_carteira, name='add_acoes_carteira'),
    path('novo/add-acoes', list_acoes_carteira, name='list_acoes_carteira'),
    path('update/<int:id>/', update_carteira, name='update_carteira'),
    path('deletar/<int:id>/', delete_carteira, name='delete_carteira')
]
