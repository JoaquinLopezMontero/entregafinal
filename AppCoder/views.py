from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from pedidos.models import *

#Vista para pagina principal
def Inicio(request):

    return render(request, "AppCoder/inicio.html")

#Vista para registrarse
def agregar_cliente(request):
    
    if request.method == 'POST':

        UserForm = UserCreationForm(request.POST)
        if UserForm.is_valid():
            UserForm.save()
        return render (request, "AppCoder/autenticacion/RespRegistro.html")
        
    else:
            UserForm = RegistroForm
        
    return render (request, "AppCoder/autenticacion/registro.html", {"UserForm":UserForm})

#Vista para Login
def iniciar_sesion(request):
    if request.method == 'POST':

        UserForm = AuthenticationForm(request, data = request.POST)
        if UserForm.is_valid():
            usuario = UserForm.cleaned_data.get("username")
            contra = UserForm.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra)

            if miUsuario:
                login(request, miUsuario)
                mensaje = f"Iniciaste sesión como {miUsuario}"

                return render (request, "AppCoder/inicio.html", {"mensaje":mensaje})
        
        else:
                mensaje = f"Error. Ingresaste mal los datos."
                return render (request, "AppCoder/inicio.html", {"mensaje":mensaje})

    else:
        UserForm = AuthenticationForm()    
    
    return render (request, "AppCoder/autenticacion/login.html", {"UserForm":UserForm})
#Vista pagina about
def nosotros(request):

    return render(request, "AppCoder/nosotros.html" )
#Vista pagina mensaje al registrarse
def registro_completo(request):
    return render(request, "AppCoder/RespRegistro.html")
#Vista editar usuario
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = editForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
    else: 
        
        form = editForm(initial={"email":usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name})
    
    return render(request, "AppCoder/autenticacion/editarperfil.html", {"editForm":form, "usuario":usuario})

#Vista pagina productos Tazas
def tazas(request):

    return render(request, "AppCoder/Tazas.html")
#Vista pagina productos Mates
def mates(request):

    return render(request, "AppCoder/Mates.html")
#Vista pagina productos Macetas
def macetas(request):

    return render(request, "AppCoder/Macetas.html")
#Vista pagina mensaje de respuesta pedido de productos
def respuesta_prod(request):
    return render(request, "AppCoder/RespuestaProd.html")

#Vista pagina con mensaje de pedido finalizado
def pedido_finalizado(request):
    return render(request, "AppCoder/Pedidos/pedidofinaliza.html")
#Vista pagina busqueda de pedidos
def buscarPedido(request):

    return render(request, "AppCoder/Pedidos/busquedaPedido.html")
#Vista para los resultados de la busqueda
def resultadoPedido(request):

    if request.method == "GET":

        nombreBusqueda = request.GET["nombre"]
        resultado = Prods.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, "AppCoder/Pedidos/resultadopedido.html", {"nombre":nombreBusqueda, "resultado":resultado })
    
    else:

        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

    

#Clases para CRUD Productos

class ProdLista(ListView):
    model = Prods
    template_name = "AppCoder/Productos/prods_list.html"

class Producto_nuevo(LoginRequiredMixin, CreateView):
    model = Prods
    template_name = "AppCoder/Productos/prods_form.html"
    success_url = "/AppCoder/respuestaprod"
    fields = ["nombre","modelo", "material", "color", "imagen"]

class Producto_Borrar(LoginRequiredMixin, DeleteView):
    model = Prods
    template_name = "AppCoder/Productos/prods_confirm_delete.html"
    success_url = "/AppCoder/Pedidos/busquedapedido/"

 #Clases para CRUD PEDIDOS
class Pedido_Borrar(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = "AppCoder/Pedidos/pedido_confirm_delete.html"
    success_url = "/AppCoder/pedido/lista"

class pedido_nuevo(LoginRequiredMixin, CreateView):
    model = Pedido
    template_name = "AppCoder/Pedidos/pedido_form.html"
    success_url = "/AppCoder/Pedidos/pedidofinaliza"
    fields = ["nombre", "producto", "cantidad", "color"]

class pedido_lista(ListView):
    model = Pedido
    template_name = "AppCoder/Pedidos/pedido_list.html"

class pedido_detalle(LoginRequiredMixin, DetailView):
    model = Prods 
    template_name = "AppCoder/Pedidos/pedido_detail.html"

class pedido_actualizar(LoginRequiredMixin, UpdateView):
    model = Pedido
    template_name = "AppCoder/Pedidos/pedido_form.html"
    success_url = "/AppCoder/Pedidos/pedidofinaliza"
    fields = ["nombre", "producto", "cantidad", "color"]

def pedirProducto(request):

    if request.method =="POST":
        form = ProdForm(request.POST, request.FILES)
        if form.is_valid():
            usuActual = Cliente.objects.get(username=request.user)
            Produs = Prods(usuario=usuActual, imagen=form.cleaned_data["imagen"])

            Produs.save()
            return render(request, "AppCoder/inicio.html")
        else:
            form = ProdForm
    return render(request, "AppCoder/pedirproducto.html", {"formulario":form})