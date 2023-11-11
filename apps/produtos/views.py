from django.shortcuts import render
from .models import Produto

def ProdutoView(request):
    view_lista = Produto.objects.all()
    return render(request, 'home.html', {'produtos': view_lista})