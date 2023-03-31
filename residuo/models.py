from django_cpf_cnpj.fields import CPFField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Pessoa(models.Model):
    cpf = CPFField(masked=True)
    nome = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False)
    telefone = PhoneNumberField(blank=True, help_text='Telefone de contato')

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=255,null=False)
    numero = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],null=False)
    bairro = models.CharField(max_length=255,null=False)
    cidade = models.CharField(max_length=255,null=False)
    cep = models.CharField(max_length=8,null=False)
    estado = models.CharField(max_length=2,null=False)
    tipo_logradouro = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.logradouro

class Categoria(models.Model):
    titulo = models.CharField(max_length=255,null=False)

    def __str__(self):
        return self.titulo
    
class Residuo(models.Model):
    TITLE_CHOICES = [
        ('Perigoso', 'Perigoso'),
        ('Não Perigoso', 'Não Perigoso')
    ]
    
    nome_residuo = models.CharField(max_length=255,null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    peculiosidade = models.CharField(max_length=255,choices=TITLE_CHOICES,null=False)

    def __str__(self):
        return self.nome_residuo

class Solicitacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    status = models.CharField(max_length=45,null=False)
    data_solicitacao = models.DateField(auto_now=False)
    hora = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    residuo= models.ForeignKey(Residuo, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.pessoa.nome + " | " + str(self.data_solicitacao)