from django.urls import path, include
from AppCoder.views import *
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView
from tienda.views import *

urlpatterns = [
    path("inicio/", Inicio, name="Start"),
    path("about/", nosotros, name="Nosotros"),
    path("registro", agregar_cliente, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/autenticacion/logout.html"), name="Logout"),
    path("RespRegistro/", registro_completo, name="Registro Completo"),
    path("autenticacion/editar/", editarUsuario, name = "Editar Usuario"),
    path("tienda/tazas", tazas, name="Tazas"),
    path("respuestaprod", respuesta_prod, name="Respuesta Prod" ),
    path("Pedidos/pedidofinaliza", pedido_finalizado, name="Pedido Finalizado"),
    path("Pedidos/busquedapedido/", buscarPedido, name="Buscar Pedido"),
    path("resultadopedido/", resultadoPedido, name="Resultados Pedidos"),
    path("resultados/", resultadoPedido, name="Busqueda Results"),
 
   #CRUD Productos

   path("prods/lista", ProdLista.as_view(), name = "Ver Productos"),
   path("prods/nuevo", Producto_nuevo.as_view(), name="Producto Nuevo"),
   path("prods/borrar/<int:pk>", Producto_Borrar.as_view(), name = "Producto Borrar"),


   #CRUD Pedidos
   path("pedido/nuevo", pedido_nuevo.as_view(), name="Pedido Nuevo"),
   path("pedido/lista", pedido_lista.as_view(), name = "Ver Pedidos"),
   path("pedido/borrar/<int:pk>", Pedido_Borrar.as_view(), name = "Pedido Borrar"),
   path("pedido/<int:pk>", pedido_detalle.as_view(), name="Pedido Detalle"),
   path("pedido/editar/<int:pk>", pedido_actualizar.as_view(), name="Pedido Actualizar"),
    
]