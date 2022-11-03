from django import forms

# Criação de Formulario
class CarteiraForm(forms.Form):
    nome = forms.CharField(max_length=200)
    acao = forms.CharField(max_length=200)
    historico = forms.CharField(max_length=200)