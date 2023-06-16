from django.shortcuts import render
from .models import Pessoa, Endereco, Residuo, Solicitacao, Categoria

def listar_pessoa(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas' : pessoas
    }
    return render(request, 'listar_index.html', context)

def listar_endereco(request):
    enderecos = Endereco.objects.all()
    context = {
        'enderecos' : enderecos
    }
    return render(request, 'listar_endereco.html', context)

def listar_residuo(request):
    residuos = Residuo.objects.all()
    context = {
        'residuos' : residuos
    }
    return render(request, 'listar_residuo.html', context)

def listar_solicitacao(request):
    solicitacoes = Solicitacao.objects.all()
    context = {
        'solicitacoes' : solicitacoes
    }
    return render(request, 'listar_solicitacao.html', context)

def listar_categoria(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias' : categorias
    }
    return render(request, 'listar_categoria.html', context)

