from django.contrib import admin
from .models import (
    Pessoa,
    Endereco,
    Solicitacao,
    Categoria,
    Residuo)
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Solicitacao)
admin.site.register(Categoria)
admin.site.register(Residuo)
