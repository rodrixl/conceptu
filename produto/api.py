from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from produto.models import Categoria, Produto 
from produto.serializers import CategoriaSerializer, ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,)
    filterset_fields = ['categoria']
    search_fields = ('nome',)