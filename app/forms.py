from socket import fromshare
from django import forms 
from django.forms import ModelForm 
from .models import *

#CREAMOS UN TEMPLATE DEL FORMULARIO


class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=4,max_length=20)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model= Producto
        fields = ['codigo','nombre','precio','stock','tipo','imagen']


class UsuarioForm(ModelForm):

    rut = forms.CharField(max_length=8)
    dv = forms.CharField(max_length=1)

    class Meta:
        model= Usuario
        fields =  ['rut','dv','pnombre','snombre','appaterno','apmaterno','correo','direccion','codigo_postal','telefono1','contrasena','imagen_usu']

        