from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

#seccion listar
def index (request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render (request,'app/index.html', datos)

def logeado(request):
    productosAll = Producto.objects.all()
    datos = {'listaProductos' : productosAll }

    # añadir producto a carro.
    if request.method =='POST':
        carro = carrito()
        carro.nombre_producto = request.POST.get('nombre_producto')
        carro.precio_producto = request.POST.get('precio_producto')
        carro.imagen = request.POST.get('imagen_producto')
        carro.save()

    return render(request,'app/logeado.html', datos)
    

#seccion agregar
def agregar(request):
    datos = {
        'form': ProductoForm()
        }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"

    return render (request,'app/agregar.html',datos)

# Añadir nuevo producto a carrito.
def CarritoCompra(request):
    CarritoALL = carrito.objects.all()

    contadorProductos = 0
    for producto in CarritoALL: 
        contadorProductos = producto.precio_producto + contadorProductos

    total = round(contadorProductos-(contadorProductos*0.05))
    datos = {
        'ItemsCarrito' : CarritoALL,
        'contadorProductos' : contadorProductos,
        'total': total
    }
    return render(request, 'app/carrito.html', datos)

# Eliminar producto existente de carrito.
def EliminarDeCarrito(request, id_producto):
    CarritoALL = carrito.objects.get(id_producto=id_producto)
    CarritoALL.delete()
    datos = {
        'ItemsCarrito' : CarritoALL
    }
    return redirect(to='carrito')

# Borrar todos los productos del carrito.
def ResetCarrito(request):
    CarritoALL = carrito.objects.all()
    CarritoALL.delete()
    
    # Volver pag carrito.
    return redirect(to='carrito')

def despacho(request):
    return render (request,'app/despacho.html')

def historial (request):
    return render (request,'app/historial.html')   
    
def modificarProducto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)    
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request,'app/modificarProducto.html', datos)

def listarProductos (request):
    productoALL = Producto.objects.all()
    datos = {
        'listaProductos' : productoALL
    }
    return render(request,'app/listarProductos.html',datos)

def eliminarProducto (request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to='listarProductos')

def perfil (request):
    return render (request,'app/perfil.html')

def producto1(request):
    return render(request, 'app/producto1.html')    

# Detalles producto.
def producto(request, codigo):

    # Busqueda prod por cod.
    producto = Producto.objects.get(codigo=codigo)

    # añadir producto a carro.
    if request.method =='POST':
        carro = carrito()
        carro.nombre_producto = request.POST.get('nombre_producto')
        carro.precio_producto = request.POST.get('precio_producto')
        carro.imagen = request.POST.get('imagen_producto')
        carro.save()

    datos = {
        'DetallesProducto': producto
    }
    return render(request, 'app/producto.html', datos)   

def seguimiento(request):
    return render (request,'app/seguimiento.html')

def signin (request):
    return render(request, 'app/signin.html')

def suscripcion (request):
    return render(request, 'app/suscripcion.html')
    
def registrarse(request):
    datos = {
        'form': UsuarioForm()
        }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario agredado correctamente!"
    return render(request, 'app/registrarse.html', datos)


def listarUsuarios(request):
    UsuarioALL = Usuario.objects.all()
    datos = {
        'listarUsuarios' : UsuarioALL
    }
    return render(request, 'app/listarUsuarios.html',datos)

def modificarUsuario (request, rut):
    usuario = Usuario.objects.get(rut=rut)
    datos = {
        'form' : UsuarioForm(instance=usuario)    
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente!'
            datos['form'] = formulario

   

    return render(request,'app/modificarUsuario.html', datos)

def eliminarUsuario (request, rut):
    usuario = Usuario.objects.get(rut=rut)
    usuario.delete()
    return redirect(to='listarUsuarios')

