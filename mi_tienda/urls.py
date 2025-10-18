from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('producto_list'), name='home'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]
