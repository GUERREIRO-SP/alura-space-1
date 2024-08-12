# pylint: disable=missing-function-docstring, missing-module-docstring
from django.urls import path
from usuarios.views import login, cadastro, logout

#.....Lista de endereços "rotas" do App galeria...
urlpatterns = [
    path("login", login, name = "login"),           #página de login.
    path("cadastro", cadastro, name = "cadastro"),  #página de cadastro de usuários.
    path("logout", logout, name = "logout"),        #página de logout.
]