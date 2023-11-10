from django.db import models
from django.contrib.auth.models import User
from apps.produtos.models import Produto  


class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name = "Pedido"
        verbose_name_plural = "Pedido"