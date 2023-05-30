from django import forms

from .models import Pessoa, Endereco, Solicitacao, Categoria, Residuo

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'email', 'telefone']

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