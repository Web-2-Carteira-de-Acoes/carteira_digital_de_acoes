from django.db import models
from carteiras.models import Carteira
# Create your models here.

class Acoes(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=20, decimal_places=2) 
    info = models.TextField() 
    codigo = models.CharField(max_length=200) 
    moeda = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.id, self.nome