from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Prods

class crearCliente(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    mail = forms.EmailField()
    
class nuevoProducto(forms.Form):
    nombre = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    material = forms.CharField(max_length=40)
    color = forms.CharField(max_length=40)

class nuevoPedido(forms.Form):
    nombre = forms.CharField(max_length=40,)
    producto = forms.CharField(max_length=40)
    cantidad = forms.IntegerField()
    color = forms.CharField(max_length=30)
    
    
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class editForm(UserCreationForm):
    
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]


