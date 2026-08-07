# Arquivo serializers responsável por transformar a requisição de informação para salvar no banco de dados no formato de tabela
# importando a biblioteca rest framework o serializers
from rest_framework import serializers
from models import Produto

# Criação de classe Serializers produtos

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "quantidade", "preco", "created_at"]