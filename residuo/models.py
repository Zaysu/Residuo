from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.CharField(max_length=45,null=False)
    nome = models.CharField(max_length=45,null=False)
    email = models.CharField(max_length=45,null=False)
    senha = models.CharField(max_length=45,null=False)
    telefone = models.CharField(max_length=45,null=False)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    pessoa_cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    rua = models.CharField(max_length=45,null=False)
    numero = models.CharField(max_length=45,null=False)
    bairro = models.CharField(max_length=45,null=False)
    cidade = models.CharField(max_length=45,null=False)
    cep = models.CharField(max_length=45,null=False)
    estado = models.CharField(max_length=45,null=False)

class Solicitacao(models.Model):
    pessoa_cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    status = models.CharField(max_length=45,null=False)
    created = models.DateTimeField(auto_now=False)

class Categoria(models.Model):
    title = models.CharField(max_length=45,null=False)

class Residuo(models.Model):
    title = models.CharField(max_length=45,null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)



