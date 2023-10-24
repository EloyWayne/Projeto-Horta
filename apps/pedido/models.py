from django.db import models
from apps.LoginUser.models import Produto  

class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    data_pedido = models.DateTimeField(auto_now_add=True)
    cliente_nome = models.CharField(max_length=100)
    endereco_entrega = models.CharField(max_length=200)

    def calcular_valor_total(self):
        valor_total = sum(produto.preco for produto in self.produtos.all())
        return valor_total

    def __str__(self):
        return f"Pedido #{self.id}"
