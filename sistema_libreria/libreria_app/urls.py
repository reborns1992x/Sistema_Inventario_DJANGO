from django.urls import path
from . import views
from libreria_app.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #Esta linea permite cargar la view creada en el inicio o raiz de la app de Django
    #Cuando se deja el primer campo vacío por defecto se interpretará que la url será la raiz de la app
    
    path('home', views.principal, name='principal'),
    path('registro_producto', views.ingresar_Registro_Producto, name='registro_producto'),
    path('modificar/<int:id>/', views.Modificar_Producto, name='modificar'),
    path('eliminar/<int:id>/', views.eliminar_Producto, name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)