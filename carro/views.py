from django.shortcuts import render
from .carro import Carro
from AppCoder.models import Producto
from django.shortcuts import redirect

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregarCarro(producto=producto)
    return redirect("Tazas")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.del_producto(producto=producto)
    return redirect("Tazas")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tazas")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tazas")