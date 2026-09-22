from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Laboratorio (models.Model):
    nome = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Ativo(models.Model):
    patrimonio = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True, null=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='ativos')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True, related_name='ativos')

    status = models.CharField(max_lengt=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patrimonio} - {self.nome}"

class Movimentacao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name="movimentacoes")
    laboratorio_origem = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True, related_name="movimentacoes_origem")
    laboratorio_destino = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, null=True, related_name="movimentacoes_destino")
    data_movimentacao = models.DateTimeField(auto_now=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Movimentação: {self.ativo.nome}"

class OrdemServico(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name="ordens_servico")
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"OS - {self.ativo.nome}"
