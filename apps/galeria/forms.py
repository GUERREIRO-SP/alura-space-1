# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ["publicada",]
        # .....Ajuste dos títulos dos campos
        labels = {
            "categoria": "Selecione a categoria",
            "descricao": "Descrição",
            "foto": "Selecione a foto",
            "usuario": "Usuário",
        }
        # .....Formatação dos campos
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "legenda": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "data_cadastro": forms.DateInput(
                format = "%d/%m/%Y",
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "usuario": forms.Select(attrs={"class":"form-control"}),
            }