#   LIB interna do Django para gerar randomicamente as chaves de acesso.
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
