from django.db import models

# Create your models here.

# Cria a classe categoria

class Categoria (models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

    
# Cria a classe chamada produto
class Produto (models.Model):
    nome = models.CharField(max_length=120) # definindo o tamanho do nome do produto com tamanho máximo de 120 caracteres
    quantidade = models.PositiveIntegerField(default=0) # quantidade do produto
    preco = models.DecimalField(max_digits=10,decimal_places=2) # definindo a qtde de digitos e casas decimais

    # Aqui através da chave relacionamos a categoria e o produto
    categoria = models.ForeignKey(
        Categoria,
        # Serve para caso exclua a categoria não exclua o produto
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "produtos"
    )
    created_at = models.DateTimeField(auto_now_add = True) # registro de tempo automático quando o produto é carregado

    
    # cria a função
    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"