from rest_framework import serializers
from produto.models import Categoria, Produto

# Serializer para as categorias de produtos

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

# Serializer para os produtos

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"



