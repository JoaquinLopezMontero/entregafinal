from django.db import models
from tienda.models import *
from pedidos.models import *

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    mail = models.EmailField()

class Prods(models.Model):

    nombre= models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    material = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    imagen= models.ImageField(upload_to="productospedidos", blank=True, default= "-")

class Pedido(models.Model):

    nombre = models.CharField(max_length=40,)
    producto = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    color = models.CharField(max_length=30)
