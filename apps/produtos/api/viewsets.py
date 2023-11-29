from rest_framework import viewsets 
from .serializers import CategoriaSerializers, ProdutoSerializers
from ..models import Categoria, Produto  # Corrigido o nome aqui

class CategoriaViewsets(viewsets.ModelViewSet): 
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.all()

class ProdutoViewsets(viewsets.ModelViewSet):  # Corrigido o nome aqui
    serializer_class = ProdutoSerializers
    queryset = Produto.objects.all()
