from django.shortcuts import render, redirect
from .forms import PessoaForm, EnderecoForm, ResiduoForm, SolicitacaoForm, CategoriaForm, LoginForm, LoginRecuperar
from residuo.models import Pessoa


def index(request):
    if request.session.get('email', False):
        email = request.session.get('email', None)
        if Pessoa.objects.filter(email=email).exists():

            usuario = Pessoa.objects.get(email=email).nome
            context = {
                'usuario': usuario
            }

            return render(request, 'index.html', context)
    else:
        return redirect('login')


def form_index(request):
    if request.method == 'GET':
        form = PessoaForm()
        context = {
            'form': form,
        }

        return render(request, 'form_index.html', context)
    else:
        form = PessoaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = PessoaForm()

        context = {
            'form': form
        }
        return render(request, 'form_index.html', context)

################ Endereco################


def form_endereco(request):
    if request.method == 'GET':
        form = EnderecoForm()
        context = {
            'form': form
        }

        return render(request, 'form_endereco.html', context)
    else:
        form = EnderecoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = EnderecoForm()

        context = {
            'form': form
        }
        return render(request, 'form_endereco.html', context)

################ Residuo################


def form_residuo(request):
    if request.method == 'GET':
        form = ResiduoForm()
        context = {
            'form': form,
        }

        return render(request, 'form_residuo.html', context)
    else:
        form = ResiduoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ResiduoForm()

            context = {
                'form': form,
            }
            return render(request, 'form_residuo.html', context)

################ Categoria ################


def form_categoria(request):
    if request.method == 'GET':
        form = CategoriaForm()
        context = {
            'form': form,
        }

        return render(request, 'form_categoria.html', context)
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = CategoriaForm()

            context = {
                'form': form,
            }
            return render(request, 'form_categoria.html', context)

################ Solicitacao ################


def form_solicitacao(request):
    if request.method == 'GET':
        form = SolicitacaoForm()
        context = {
            'form': form,
        }

        return render(request, 'form_solicitacao.html', context)
    else:
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = SolicitacaoForm()

            context = {
                'form': form,
            }
            return render(request, 'form_solicitacao.html', context)

################ LOGIN ################


def form_login(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {
            'form': form
        }

        return render(request, 'login.html', context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email")
            senha = request.POST.get("senha")
            if Pessoa.objects.filter(email=email).filter(senha=senha):
                # pega u usuario
                User_ok = Pessoa.objects.get(email=email)
                # cria uma sessao para ele
                user_id = request.session['email'] = User_ok.email
                return redirect("index")
            else:
                return redirect("login")

        context = {
            'form': form
        }
        return render(request, 'login.html', context)


################ FORGOT ################
def views_recuperar_senha(request):
    if request.method == 'GET':
        form = LoginRecuperar()
        context = {
            'form': form
        }

        return render(request, 'recuperar_senha.html', context)
    else:
        form = LoginRecuperar(request.POST)
        context = {
            'form': form
        }
        return render(request, 'recuperar_senha.html', context)

################ LOGOUT ################

def Logout(request):

    if request.session.get('email'):
        del request.session['email']
    return redirect("login")
