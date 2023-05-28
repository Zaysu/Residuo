from rest_framework import serializers
from residuo import models

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Solicitacao
        fields = '__all__'
    
class ResiduoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Residuo
        fields = '__all__'