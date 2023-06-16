from django.shortcuts import render
from .models import Pessoa, Endereco, Residuo, Solicitacao, Categoria
from django.core.paginator import Paginator

def listar_pessoa(request):
    pessoas = Pessoa.objects.all()
    paginacao = Paginator(pessoas, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginacao.get_page(numero_pagina)
    context = {
        'pagina' : pagina
    }
    return render(request, 'listar_index.html', context)

def listar_endereco(request):
    enderecos = Endereco.objects.all()
    paginacao = Paginator(enderecos, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginacao.get_page(numero_pagina)
    context = {
        'pagina' : pagina
    }
    return render(request, 'listar_endereco.html', context)

def listar_residuo(request):
    residuos = Residuo.objects.all()
    paginacao = Paginator(residuos, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginacao.get_page(numero_pagina)
    context = {
        'pagina' : pagina
    }
    return render(request, 'listar_residuo.html', context)

def listar_solicitacao(request):
    solicitacoes = Solicitacao.objects.all()
    paginacao = Paginator(solicitacoes, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginacao.get_page(numero_pagina)
    context = {
        'pagina' : pagina
    }
    return render(request, 'listar_solicitacao.html', context)

def listar_categoria(request):
    categorias = Categoria.objects.all()
    paginacao = Paginator(categorias, 3)
    numero_pagina = request.GET.get('page')
    pagina = paginacao.get_page(numero_pagina)
    context = {
        'pagina' : pagina
    }
    return render(request, 'listar_categoria.html', context)