from django.urls import path
from galeria.views import index, imagem

#.....Lista de endereços "rotas" do App galeria...
urlpatterns = [
    path("", index, name = "index"),            #página principal do App galeria.
    path("/imagem", imagem, name = "imagem")    #página de imagens.
]