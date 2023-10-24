from django.db import models

class Tipo_Produtor(models.Model):
    tipo_produtor = models.CharField( max_length=100)
    
    def __str__(self):
        return self.tipo_produtor

    class Meta():
        verbose_name = "Tipo Produtor"
        verbose_name_plural = "Tipo Produtor"

class Produtor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereço = models.CharField(max_length=200, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    tipo_de_produtor = models.ForeignKey(Tipo_Produtor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome
    class Meta():
        verbose_name = "Produtor"
        verbose_name_plural = "Produtor"


class Categoria(models.Model):
    categoria = models.CharField( max_length=100)
    
    def __str__(self):
        return self.categoria

    class Meta():
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    produtor = models.ForeignKey(Produtor, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.nome
    class Meta():
        verbose_name = "Produto"
        verbose_name_plural = "Produto"