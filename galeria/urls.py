from django.urls import path
from galeria.views import index, imagem, buscar

#.....Lista de endereços "rotas" do App galeria...
urlpatterns = [
    path("", index, name = "index"),                            #página principal do App galeria.
    path("imagem/<int:foto_id>", imagem, name = "imagem"),      #página de imagens.
    path("buscar", buscar, name = "buscar"),                    #página de busca.
]