from django import forms

from .models import Pessoa, Endereco, Solicitacao, Categoria, Residuo

class PessoaForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Pessoa
        fields = ['cpf', 'nome', 'email', 'senha', 'telefone']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['pessoa_cpf', 'rua', 'numero', 'bairro', 'cidade', 'cep', 'estado']

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['pessoa_cpf', 'status', 'created']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['title']

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['title', 'categoria', 'solicitacao']