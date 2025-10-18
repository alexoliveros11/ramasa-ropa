from django.urls import path, include
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Rutas para la API REST
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    # Rutas web
    path('', ProductoListView.as_view(), name='producto_list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),

    # Rutas API (ahora separadas)
    path('api/', include(router.urls)),
]
