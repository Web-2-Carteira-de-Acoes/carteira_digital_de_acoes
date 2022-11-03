from django import forms

class Acoes(forms.Form):
    nome = forms.CharField(max_length=200)
    valor_atual = forms.CharField(max_length=200)
    quantidade_atual = forms.CharField(max_length=200)
    sigla = forms.CharField(max_length=200) 
    historico = forms.CharField(max_length=200)
    transacao = forms.CharField(max_length=200)