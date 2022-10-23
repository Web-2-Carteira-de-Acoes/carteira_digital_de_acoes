
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from . import views

#  Rotas, para a APP de usuário

urlpatterns = [
    path('', TemplateView.as_view(template_name="acoes/acoes.html")),
]
