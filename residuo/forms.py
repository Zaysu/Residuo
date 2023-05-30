from django import forms

from .models import Pessoa, Endereco, Solicitacao, Categoria, Residuo

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'email','senha', 'telefone']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero', 'bairro', 'cidade', 'cep', 'estado' ,'tipo_logradouro']

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['pessoa', 'status', 'data_solicitacao', 'hora', 'residuo', 'endereco']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['titulo']

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['nome_residuo', 'categoria', 'peculiosidade']
        

class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {'class': 'form-control login-input ', })

    class Meta:
        model = Pessoa
        fields = ['email', 'senha']
        labels = {
            'email': 'Email:',
            'senha': 'Senha:',
        }
class LoginRecuperar(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginRecuperar, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update(
                {'class': 'form-control login-input ', })

    class Meta:
        model = Pessoa
        fields = ['email']
        labels = {
            'email': 'Email:',
        }