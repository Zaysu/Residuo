from django_cpf_cnpj.fields import CPFField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Pessoa(models.Model):
    cpf = CPFField(masked=True)
    nome = models.CharField(max_length=255,null=False,blank=False, verbose_name='Nome')
    email = models.EmailField(max_length=255,null=False,blank=False, verbose_name='E-mail')
    senha = models.CharField(max_length=255,null=False,blank=False, verbose_name='Senha')
    telefone = PhoneNumberField(blank=True, help_text='Telefone de contato', verbose_name='Telefone')
    def __str__(self):
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255,null=False, verbose_name='Logradouro')
    numero = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],null=False)
    bairro = models.CharField(max_length=255,null=False, verbose_name='Bairro')
    cidade = models.CharField(max_length=255,null=False, verbose_name='Cidade')
    cep = models.CharField(max_length=8,null=False, verbose_name='CEP')
    estado = models.CharField(max_length=2,null=False, verbose_name='Estado')
    tipo_logradouro = models.CharField(max_length=255,null=False, verbose_name='Tipo de Logradouro')

    def __str__(self):
        return self.logradouro

class Categoria(models.Model):
    titulo = models.CharField(max_length=255,null=False, verbose_name='Título')

    def __str__(self):
        return self.titulo
    
class Residuo(models.Model):
    TITLE_CHOICES = [
        ('Perigoso', 'Perigoso'),
        ('Não Perigoso', 'Não Perigoso')
    ]
    
    nome_residuo = models.CharField(max_length=255,null=False, verbose_name='Nome do Resíduo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    peculiosidade = models.CharField(max_length=255,choices=TITLE_CHOICES,null=False, verbose_name='Peculiosidade')

    def __str__(self):
        return self.nome_residuo

class Solicitacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    status = models.CharField(max_length=45,null=False, verbose_name='Status')
    data_solicitacao = models.DateField(auto_now=False, verbose_name='Data da Solicitação')
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=False, verbose_name='Hora')
    residuo= models.ForeignKey(Residuo, on_delete=models.CASCADE, verbose_name='Resíduo')
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name='Endereço')

    def __str__(self):
        return self.pessoa.nome + " | " + str(self.data_solicitacao)