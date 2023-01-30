from django.db import models
from usuarios.models import User


# Create your models here.

class Carteira(models.Model):
    nome = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    historico = models.CharField(max_length=200)
    

    def __str__(self):
        return self.id, self.nome 