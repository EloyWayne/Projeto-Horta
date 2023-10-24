from django.db import models
from apps.LoginUser.models import Produto  

class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    data_pedido = models.DateTimeField(auto_now_add=True)
    cliente_nome = models.CharField(max_length=100)
    endereco_entrega = models.CharField(max_length=200)

    def __str__(self):
        return self.cliente_nome
