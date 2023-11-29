from rest_framework import serializers 
from ..models import DadosPessoais 

# Forma 1 
class DadosPessoaisSerializers(serializers.ModelSerializer):
    class Meta: 
       model = DadosPessoais
       fields = "__all__" 
