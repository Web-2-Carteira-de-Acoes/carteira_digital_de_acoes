from django import forms
from .models import Carteira_Acoes





class Carteira_AcoesForm(forms.ModelForm):
    class Meta:
        model = Carteira_Acoes
        fields = "__all__"