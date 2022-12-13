from django import forms
from .models import Acoes





class AcoesForm(forms.ModelForm):
    class Meta:
        model = Acoes
        fields = "__all__"