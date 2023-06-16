from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PessoaForm, EnderecoForm, ResiduoForm, SolicitacaoForm, CategoriaForm
from .models import Solicitacao


def index(request):
    return render(request, 'index.html')

@login_required
def form_index(request):
    if request.method == 'GET':
        form = PessoaForm()
        context = {
            'form' : form
        }
        
        return render(request, 'form_index.html', context)
    else:
        form = PessoaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = PessoaForm()
        
        context = {
            'form' : form
        }
        return render(request, 'form_index.html', context)
    
################Endereco################
@login_required
def form_endereco(request):
    if request.method == 'GET':
        form = EnderecoForm()
        context = {
            'form' : form
        }
        
        return render(request, 'form_endereco.html', context)
    else:
        form = EnderecoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = EnderecoForm()
        
        context = {
            'form' : form
        }
        return render(request, 'form_endereco.html', context)   
    
################Residuo################
@login_required
def form_residuo(request):
    if request.method == 'GET':
        form = ResiduoForm()
        context = {
            'form' : form,
        }
        
        return render(request, 'form_residuo.html', context)
    else:
        form = ResiduoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ResiduoForm()
            
            context = {
                'form' : form,
            }
            return render(request, 'form_residuo.html', context)
        
################Categoria################
@login_required
def form_categoria(request):
    if request.method == 'GET':
        form = CategoriaForm()
        context = {
            'form' : form,
        }
        
        return render(request, 'form_categoria.html', context)
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = CategoriaForm()
            
            context = {
                'form' : form,
            }
            return render(request, 'form_categoria.html', context)
        
################Solicitacao################
def form_solicitacao(request):
    if request.method == 'GET':
        form = SolicitacaoForm()
        context = {
            'form' : form,
        }
        
        return render(request, 'form_solicitacao.html', context)
    else:
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = SolicitacaoForm()
            
            context = {
                'form' : form,
            }
            return render(request, 'form_solicitacao.html', context)
       
def editar_solicitacao(request,id):
    data = {}
    solicitacao = Solicitacao.objects.get(id = id)
    form = SolicitacaoForm(request.POST or None, instance=solicitacao)
    data['solicitacao'] = solicitacao
    data['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_solicitacao')
    else:
        return render(request, 'editar_solicitacao.html', data)