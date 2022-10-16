from random import choices
from django import forms


class MeuFormulario(forms.Form):

    choices_questao = ( ('Q001' ,'Escolaridade do Pai'),
                        ('TP_SEXO', 'Comparar Nota ao Sexo'))
            
    choices_sexo = (('outros' ,'Outros'),    
                    ('f', 'Filtrar Apenas Femilino'),
                    ('m' ,'Filtrar Apenas Masculino'))


    questao = forms.ChoiceField(choices=choices_questao)
    sexo = forms.ChoiceField(choices=choices_sexo)