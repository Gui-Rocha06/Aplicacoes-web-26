from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=120) # definindo o tamanho do nome do produto com tamanho máximo de 120 caracteres
    quantidade = models.PositiveIntegerField(default=0) # quantidade do produto
    preco = models.DecimalField(max_digits=10,decimal_places=2) # definindo a qtde de digitos e casas decimais
    created_at = models.DateTimeField(auto_now_add = True) # registro de tempo automático quando o produto é carregado


    # cria a função
    def __str__(self):
        return f"{self.nome} (qtde={self.quantidade})"