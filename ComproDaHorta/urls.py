from django.contrib import admin
from django.urls import path, include
from apps.core.api.viewsets import DadosPessoaisViewsets
from apps.pedido.api.viewsets import PedidoViewsets
from apps.produtos.api.viewsets import CategoriaViewsets,ProdutoViewsets
from rest_framework import routers

# CONFIGURAÇÃO DOS ARQUIVOS ESTÁTICOS
from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter() 
route.register('DadosPessoais', DadosPessoaisViewsets, basename = 'DadosPessoais')
route.register('Pedido', PedidoViewsets, basename = 'Pedido')
route.register('Categoria', CategoriaViewsets, basename = 'Categoria')
route.register('Produto', ProdutoViewsets, basename = 'Produto')

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path("", include(route.urls), name="Core"),
    path('', include('apps.produtos.urls')),
    path('core/', include('apps.core.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # CONFIGURAÇÃO DOS ARQUIVOS ESTÁTICOS
