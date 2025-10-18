from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from .forms import ProductoForm  # ← Importación del formulario personalizado

# Vistas basadas en clases para el CRUD web
class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm  # ← Usamos el formulario personalizado
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm  # ← Usamos el formulario personalizado
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

# Vista para la API REST
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
