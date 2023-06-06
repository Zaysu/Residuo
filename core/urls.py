from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
#from residuo.api import viewsets as residuoviewsets
from residuo.api.viewsets import PessoaViewSet, EnderecoViewSet, CategoriaViewSet, SolicitacaoViewSet, ResiduoViewSet

route = routers.DefaultRouter()
route.register(r'API-pessoa', PessoaViewSet, basename='Pessoa')
route.register(r'API-endereco', EnderecoViewSet, basename='Endereco')
route.register(r'API-categoria', CategoriaViewSet, basename='Categoria')
route.register(r'API-solicitacao', SolicitacaoViewSet, basename='Solicitacao')
route.register(r'API-residuo', ResiduoViewSet, basename='Residuo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('residuo.urls')),
    path('', include(route.urls)),
    path("accounts/", include("django.contrib.auth.urls")),

]
