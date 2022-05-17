from distutils.command.upload import upload
from django.db import models

# Create your models here.

class TipoProducto (models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table='db_tipo_producto'

class Producto (models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=80)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete = models.CASCADE)#models.PROTECT
    imagen = models.ImageField(upload_to="productos", null = True)
    fecha_ingreso = models.DateField(auto_now_add = True)
    create_at= models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now = True)
    


    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_producto'

class Usuario (models.Model):
    rut = models.IntegerField(null=False,primary_key=True)
    dv = models.IntegerField()
    pnombre = models.CharField(max_length=20)
    snombre = models.CharField(max_length=20)
    appaterno = models.CharField(max_length=20)
    apmaterno = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=90)
    codigo_postal = models.IntegerField()
    telefono1 = models.IntegerField()
    contrasena = models.CharField(max_length=20)
    imagen_usu = models.ImageField(upload_to="perfil", null = True)

    def __str__(self):
        return self.pnombre

    

class carrito(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=40)
    precio_producto = models.IntegerField()
    imagen = models.ImageField(upload_to="carrito", null = True)

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_carrito'