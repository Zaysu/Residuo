from rest_framework import viewsets
from residuo.api import serializers
from residuo import models

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = models.Pessoa.objects.all()
    serializer_class = serializers.PessoaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = models.Endereco.objects.all()
    serializer_class = serializers.EnderecoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Solicitacao.objects.all()
    serializer_class = serializers.SolicitacaoSerializer

class ResiduoViewSet(viewsets.ModelViewSet):
    queryset = models.Residuo.objects.all()
    serializer_class = serializers.ResiduoSerializer