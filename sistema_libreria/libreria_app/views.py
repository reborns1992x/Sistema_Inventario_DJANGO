from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registro_Producto
from .formularios import registro_Producto_Form

def principal (request):
    productos_listados = registro_Producto.objects.all()
    
    return render (request, 'productos/index.html', {'productos':productos_listados})
 
    
def ingresar_Registro_Producto(request):
    if request.method == 'POST':
        formulario = registro_Producto_Form(request.POST or None, request.FILES or None)
        print (formulario)    
        if formulario.is_valid():
            formulario.save()
            return redirect('principal')
    else:
        formulario = registro_Producto_Form()    
    return render (request, 'productos/registro.html', {'formulario': formulario})
    
def eliminar_Producto(request, id):
    productos_listados = registro_Producto.objects.get(id=id)
    productos_listados.delete()
    return redirect('principal')

def Modificar_Producto(request,id):
    productos_listados = registro_Producto.objects.get(id=id)
    formulario = registro_Producto_Form(request.POST or None, request.FILES or None, instance=productos_listados)
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect('principal')
    return render (request, 'productos/modificar.html', {'formulario': formulario})


    
    