from django.db import models
from acoes.models import Acoes
from carteiras.models import Carteira

# Create your models here.
class Carteira_Acoes(models.Model):
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acoes, on_delete=models.PROTECT)
    quantidade_atual = models.CharField(max_length=200)
    precoPago = models.DecimalField(max_digits=20, decimal_places=2) 
    dataCompra = models.TextField()
    
        
    def __str__(self):
        
        return str(self.carteira)
    
    
    


    
    