from rest_framework import serializers 
from ..models import Categoria,Produto

# Forma 1 
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Categoria
       fields = "__all__"

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Produto
       fields = "__all__"