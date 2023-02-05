from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Carteira(models.Model):
    nome = models.CharField(max_length=200)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
         return f'{self.id} {self.nome} '
    


