from django.db import models

# Create your models here.

class Acoes(models.Model):
    nome = models.CharField(max_length=200)
    valor_atual = models.CharField(max_length=200)
    quantidade_atual = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200) 
    
    def __self__(self):
        return self.nome