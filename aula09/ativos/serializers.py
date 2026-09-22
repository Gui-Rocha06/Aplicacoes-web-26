from rest_framework import serializers
from .models import (
    Categoria,
    Laboratorio,
    Ativo,
    Movimentacao,
    OrdemServico
)

# Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


# Laboratório
class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = "__all__"


# Ativo
class AtivoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(
        source="categoria.nome", 
        read_only=True
    )
    laboratorio_nome = serializers.CharField(
        source="laboratorio.nome", 
        read_only=True
    )

    class Meta:
        model = Ativo
        fields = [
            "id",
            "patrimonio",
            "nome",
            "descricao",
            "categoria",         
            "categoria_nome",   
            "laboratorio",       
            "laboratorio_nome",  
            "status",
            "ativo"
        ]


# Movimentação
class MovimentacaoSerializer(serializers.ModelSerializer):
    ativo_nome = serializers.CharField(
        source="ativo.nome", 
        read_only=True
    )
    origem_nome = serializers.CharField(
        source="laboratorio_origem.nome", 
        read_only=True
    )
    destino_nome = serializers.CharField(
        source="laboratorio_destino.nome", 
        read_only=True
    )

    class Meta:
        model = Movimentacao
        fields = [
            "id",
            "ativo",
            "ativo_nome",
            "laboratorio_origem",
            "origem_nome",
            "laboratorio_destino",
            "destino_nome",
            "data_movimentacao",
            "observacao"
        ]
        
        read_only_fields = [
            "data_movimentacao"
        ]


# Ordem de Serviço
class OrdemServicoSerializer(serializers.ModelSerializer):
    ativo_nome = serializers.CharField(
        source="ativo.nome", 
        read_only=True
    )

    class Meta:
        model = OrdemServico
        fields = [
            "id",
            "ativo",
            "ativo_nome",
            "descricao",
            "status",
            "data_abertura",
            "data_fechamento"
        ]
        
        read_only_fields = [
            "data_abertura"
        ]