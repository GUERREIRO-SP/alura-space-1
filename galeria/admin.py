from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "data_cadastro", "publicada", "categoria", "nome", "foto", "legenda")
    list_display_links = ("id", "nome")         # coloca o campo como link, para acesso ao registro para edição
    search_fields = ("nome", )                  # inserir uma "tupla" para criar campos de pesquisa
    list_filter = ("categoria", "usuario", )    # inserir uma "tupla" para criar campos de filtro
    list_editable = ("publicada", )
    list_per_page = 10                          # mostra 10 linhas por página no Django/Admin
    
admin.site.register(Fotografia, ListandoFotografias)