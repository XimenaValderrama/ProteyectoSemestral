from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','precio','stock','tipo','imagen']
    search_fields = ['codigo', 'nombre']
    list_editable =['precio']
    list_per_page = 4

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id_producto','nombre_producto','precio_producto','imagen']
    search_fields = ['id_producto', 'nombre_producto']
    list_per_page = 4

admin.site.register(carrito, CarritoAdmin)


class AgregarUsu(admin.ModelAdmin):
    list_display = ['rut','dv','pnombre','snombre','appaterno','apmaterno','direccion','codigo_postal','telefono1','contrasena','imagen_usu']
    search_fields = ['rut']
    list_per_page = 4

admin.site.register(Usuario,AgregarUsu)
