# pylint: disable=missing-function-docstring, missing-module-docstring
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Cria a estrutura da tabela que contém informações das fotos...
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("NEBULOSA", "Nebulosa"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null = False, blank = False)
    legenda = models.CharField(max_length=150, null = False, blank = False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')  # Cria um combo...
    descricao = models.TextField(null = False, blank = False)
    # foto = models.CharField(max_length=100, null = False, blank = False)
    # versão do treinamento, inserindo pastas Y/M/D
    # foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank = True)
    # será criada a pasta '/media/fotos/', no dir.principal, que conterá o upload das fotos
    foto = models.ImageField(upload_to="fotos/", blank = True)
    publicada = models.BooleanField(default = True)    # checkbox de publicação.
    data_cadastro = models.DateTimeField(default=datetime.now, blank = False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

def __str__(self):
    return f"Fotografia: [nome={self.nome}]"