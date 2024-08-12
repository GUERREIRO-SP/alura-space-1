# pylint: disable=missing-function-docstring, missing-module-docstring
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from galeria.models import Fotografia

def index(request):

    # Valida se o usuário está logado no App...
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado...")
        return redirect("login")

    # Mostra todos os objetos da tabela
    # fotografias = Fotografia.objects.all()
    # order_by – ordena os registros pelo campo informado      ( '-' DESC )
    # filter – mostra apenas os registros com ‘publicado=true’

    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicada = True)
    return render(request, "galeria/index.html", {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicada = True)

    if "buscar" in request.GET:

        # Valida se o usuário está logado no App...
        if not request.user.is_authenticated:
            messages.error(request, "Usuário não logado...")
            return redirect("login")

        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})
