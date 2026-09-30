from django.db import models

# Create your models here.
# Cria a classe chamada produto
class Produto(models.Model):
    nome = models.CharField(max_length=120) # definindo o tamanho do nome do produto com tamanho máximo de 120 caracteres
    quantidade = models.PositiveIntegerField(default=0) # quantidade do produto
    preco = models.DecimalField(max_digits=1, decimal_places=2) # definindo a quantidade de casas do preço do produto e o número de casas decimais
    created_at = models.DateTimeFeld(auto_now_add=True) # registro de tempo automático quando o produto é carregado


    # Cria a função

    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"