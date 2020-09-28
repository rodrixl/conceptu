from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from produto.api import CategoriaViewSet, ProdutoViewSet

api_router = routers.DefaultRouter()
api_router.register(r'categoria', CategoriaViewSet)
api_router.register(r'produto', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
