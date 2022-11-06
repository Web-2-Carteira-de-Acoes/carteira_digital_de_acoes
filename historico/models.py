from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from matplotlib.rcsetup import validate_int_or_None
from numpy import integer, place

# Create your models here.

class Historico(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True)
    lucro = models.DecimalField(max_digits=5, decimal_places=2)
    compremento = models.CharField(max_length=150)
          
    def __str__(self):
        return self.Historico

