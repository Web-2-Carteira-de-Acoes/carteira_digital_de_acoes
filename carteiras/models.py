from django.db import models

# Create your models here.

class Carteira(models.Model):
    nome = models.CharField(max_length=200)
    acao = models.CharField(max_length=200)
    historico = models.CharField(max_length=200)

