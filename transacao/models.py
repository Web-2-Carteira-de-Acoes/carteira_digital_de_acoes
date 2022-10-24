from django.db import models

# Create your models here.


class Transacao(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2) 
    quantidade = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.Transacao
    