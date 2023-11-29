from rest_framework import serializers 
from ..models import Pedido 

# Forma 1 
class PedidoSerializers(serializers.ModelSerializer):
    class Meta: 
       model = Pedido
       fields = "__all__"