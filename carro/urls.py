from django.urls import path
from AppCoder.views import *
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from carro.views import *

app_name="carro"
urlpatterns = [

    path("agregar/<int:producto_id>/", agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", restar_producto, name="restar"),
    path("limpiar/<int:producto_id>/", limpiar_carro, name="limpiar"),
    
    
    path("inicio/", Inicio, name="Start"),
    path("about/", nosotros, name="Nosotros"),
    path("registro", agregar_cliente, name="Sign Up"),
    path("login/", iniciar_sesion, name="Sign In"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/autenticacion/logout.html"), name="Logout"),
    path("RespRegistro/", registro_completo, name="Registro Completo"),
    path("autenticacion/editar/", editarUsuario, name = "Editar Usuario"),
    path("tazas", tazas, name="Tazas"),
    path("mates", mates, name="Mates"),
    path("macetas", macetas, name="Macetas"),
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
  
   path("pedido/lista", pedido_lista.as_view(), name = "Ver Pedidos"),
   path("pedido/borrar/<int:pk>", Pedido_Borrar.as_view(), name = "Pedido Borrar"),
   path("pedido/<int:pk>", pedido_detalle.as_view(), name="Pedido Detalle"),
  
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)