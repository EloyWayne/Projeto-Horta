from rest_framework import viewsets
from .serializers import DadosPessoaisSerializers  # Corrigido o nome aqui
from ..models import DadosPessoais

class DadosPessoaisViewsets(viewsets.ModelViewSet):
    serializer_class = DadosPessoaisSerializers  # Corrigido o nome aqui
    queryset = DadosPessoais.objects.all()
