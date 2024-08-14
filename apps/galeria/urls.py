from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro
#.....Lista de endereços "rotas" do App galeria...
urlpatterns = [
    path("", index, name = "index"),                                #página principal do App galeria.
    path("imagem/<int:foto_id>", imagem, name = "imagem"),          #página de imagens.
    path("buscar", buscar, name = "buscar"),                        #página de busca.
    path("nova-imagem", nova_imagem, name = "nova_imagem"),         #página de inclusão novas imagens.
    path("editar-imagem/<int:foto_id>", editar_imagem, name = "editar_imagem"),     #página de edição de imagens.
    path("deletar-imagem/<int:foto_id>", deletar_imagem, name = "deletar_imagem"),  #página de exclusão de imagens.
    path("filtro/<str:categoria>", filtro, name = "filtro"),                        #página para aplicar filtros.
]