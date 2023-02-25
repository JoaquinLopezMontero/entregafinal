from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from flask import redirect
from pedidos.models import Pedidos, LineaPedido
from carro.carro import Carro
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url="AppCoder/autenticacion/login")
def procesar_pedido(request):
    pedido=Pedidos.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    return render (request, "AppCoder/Pedidos/pedidofinaliza.html")
   