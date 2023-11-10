from django.db import models

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria
    
    class Meta():
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
        
    class Meta():
        verbose_name = "Produto"
        verbose_name_plural = "Produto"