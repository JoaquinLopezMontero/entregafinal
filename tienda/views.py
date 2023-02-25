from django.shortcuts import render
from .models import Producto


def tazas(request):

    productos=Producto.objects.all()

    return render(request, "tienda/Tazas.html", {"productos":productos})
