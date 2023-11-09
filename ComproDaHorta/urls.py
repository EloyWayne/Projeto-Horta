from django.contrib import admin
from django.urls import path, include

# CONFIGURAÇÃO DOS ARQUIVOS ESTÁTICOS
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.produtos.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # CONFIGURAÇÃO DOS ARQUIVOS ESTÁTICOS
