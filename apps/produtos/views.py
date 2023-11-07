from django.shortcuts import render
from .models import Pedido

def PedidoView(request):
    view_lista = Pedido.objects.all()
    return render(request, 'core.html', {'Pedido': view_lista})