
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from .views import create_usuario, delete_usuario, list_usuarios, update_usuario

#  Rotas, para a APP de usuário

urlpatterns = [
    path('', list_usuarios, name='list_usuarios'),
    path('novo', create_usuario, name='create_usuarios'),
    path('update/<int:id>/', list_usuarios, name='update_usuario'),
    path('deletar/<int:id>/', delete_usuario, name='delete_usuario'),
]
