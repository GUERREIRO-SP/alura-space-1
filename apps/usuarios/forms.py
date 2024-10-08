# pylint: disable=missing-function-docstring, missing-module-docstring
from django import forms

class LoginForms(forms.Form):
    """ Classe de controle do Login"""
    nome_login = forms.CharField(
        label = "Nome de login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    """Classe de controle do Cadastro"""
    nome_cadastro = forms.CharField(
        label = "Nome de cadastro",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email = forms.EmailField(
        label = "Email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Joaosilva@xxxx.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label = "Confirme a senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo!")
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        # ..... Valida se a senha é diferente
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não conferem!")
            else:
                return senha_2
