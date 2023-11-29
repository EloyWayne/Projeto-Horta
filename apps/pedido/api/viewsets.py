from rest_framework import viewsets 
from .serializers import PedidoSerializers
from ..models import Pedido

class PedidoViewsets(viewsets.ModelViewSet): 
  serializer_class = PedidoSerializers
  queryset = Pedido.objects.all()
