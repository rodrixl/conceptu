from django.contrib import admin
from produto.models import Categoria, Produto

# ModelAdmin das classes, para ter a opcao de utilizar o admin também para criar/editar objetos

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
