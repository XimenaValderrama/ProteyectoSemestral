from .views import *
from django.urls import path


urlpatterns=[
    path('',index,name='index'),
    path('carrito', CarritoCompra, name='carrito'),
    path('despacho',despacho, name='despacho'),
    path('historial',historial,name='historial'),
    path('logeado',logeado,name='logeado'),
    path('perfil',perfil ,name='perfil'),
    path('producto1',producto1 ,name='producto1'),
    path('seguimiento',seguimiento ,name='seguimiento'),
    path('signin', signin,name='signin'),
    path('registrarse',registrarse, name= 'registrarse'),
    path('suscripcion',suscripcion ,name='suscripcion'),
    path('agregar',agregar,name='agregar'),
    path('modificarProducto/<codigo>/',modificarProducto,name='modificarProducto'),
    path('listarProductos/',listarProductos,name='listarProductos'),
    path('eliminarProducto/<codigo>/',eliminarProducto,name='eliminarProducto'),
    path('EliminarDeCarrito/<id_producto>/',EliminarDeCarrito, name= 'EliminarDeCarrito'),
    path('ResetCarrito/', ResetCarrito, name='ResetCarrito'),
    path('listarUsuarios/', listarUsuarios, name='listarUsuarios'),
    path('eliminarUsuario/<rut>/', eliminarUsuario, name='eliminarUsuario'),
    path('modificarUsuario/<rut>/', modificarUsuario, name='modificarUsuario'),
    path('producto/<codigo>/', producto, name='producto'),
]