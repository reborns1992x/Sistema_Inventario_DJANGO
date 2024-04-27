from typing import Any
from django.db import models
from django.utils import timezone
from .choices import OPCIONES
class clasificacionProducto(models.Model):

    lista_Clasificacion_Producto = models.CharField(max_length=150,choices=OPCIONES, default="1")
    
    def __str__(self):
       return dict(OPCIONES)[self.lista_Clasificacion_Producto]
    

class registro_Producto(models.Model):
    id= models.AutoField(primary_key=True)
    nombre_Producto = models.CharField(max_length=100, verbose_name="Nombre del producto")
    cantidad_Producto = models.IntegerField(default=0, verbose_name="Cantidad del producto")
    costo_Producto = models.IntegerField(default=0, verbose_name="Costo del producto")
    clasificacion_Producto = models.ForeignKey(clasificacionProducto,on_delete=models.CASCADE,default="",verbose_name="Tipo de producto")
    imagen_Producto = models.ImageField(upload_to='imagen_producto/', null=True, verbose_name="Imagen del producto" )
    descripcion_Producto= models.CharField(max_length=100,verbose_name="Descripción del producto")
    

    def __str__(self):
        fila = "Producto: " + self.nombre_Producto + " - " + "Descripción: " + self.descripcion_Producto
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen_Producto.storage.delete(self.imagen_Producto.name)
        super().delete()
        """Función que sirve para borrar la imagen cuando se borra el registro
            Por defecto no lo hace sin estas lineas de código."""   
    