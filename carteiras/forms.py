from django import forms
from .models import Carteira
# Criação de Formulario

    
    
    
class CarteiraForm(forms.ModelForm):
    class Meta:
        model = Carteira
        fields = "__all__"