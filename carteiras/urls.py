
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import create_carteira, delete_carteira, list_carteiras, update_carteira

#  Rotas, para a APP de Carteira

urlpatterns = [
    path('', list_carteiras, name='list_carteiras'),
    path('novo', create_carteira, name='create_carteira'),
    path('update/<int:id>/', update_carteira, name='update_carteira'),
    path('deletar/<int:id>/', delete_carteira, name='delete_carteira'),
]
