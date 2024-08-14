# pylint: disable=missing-function-docstring, missing-module-docstring
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

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

    return render(request, "galeria/index.html", {"cards": fotografias})

def nova_imagem(request):
    # Valida se o usuário está logado no App...
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado...")
        return redirect("login")

    form = FotografiaForms
    # Valida se estamos editando o formulário
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        # Verifica se o formulario foi preenchido corretamente
        if form.is_valid():
            form.save()
            messages.success(request, "Registro cadastrado!")
            return redirect("index")

    return render(request, "galeria/nova_imagem.html", {"form": form})

def editar_imagem(request, foto_id):
    #  Lê as informações do registro (ID) no DB.sqlite3
    fotografia = Fotografia.objects.get(id=foto_id)
    #  Atribui os dados do ítem ao formulário
    form = FotografiaForms(instance=fotografia)

    if request.method =="POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro editado com sucesso!")
            return redirect("index")

    return render(request, "galeria/editar_imagem.html", {"form": form, "foto_id": foto_id})

def deletar_imagem(request, foto_id):
    #  Lê as informações do registro (ID) no DB.sqlite3
    fotografia = Fotografia.objects.get(id=foto_id) 
    fotografia.delete()
    messages.success(request, "Deleção bem sucedida!")
    return redirect("index")

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("-data_cadastro").filter(publicada = True, categoria=categoria)
    return render(request, "galeria/index.html", {"cards": fotografias})
