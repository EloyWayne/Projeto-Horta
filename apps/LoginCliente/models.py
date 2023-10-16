from django.db import models
from django.contrib.auth.models import User

class DadosPessoais(models.Model):
    endereço = models.CharField(max_length=200)
    telofone = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.endereço
