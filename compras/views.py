from django.shortcuts import render,redirect
from compras.forms import ClienteForms,ProductoForms,DetalleForms,FacturaForms
# Create your views here.
from compras.models import Cliente,Producto,Factura,Detalle_factura
from django.http import HttpResponse


def crear_cliente(request):
    if request.method == 'GET':
        formulario = ClienteForms()
        contexto = {
            'formulario': formulario
        }
        return render(request, "crear_cliente.html", contexto)
    else:
        formulario = ClienteForms(request.POST)
        contexto = {
            'form': formulario
        }
        # print(formulario)
        if formulario.is_valid():
            formulario.save()
        return redirect('consulta_cliente')

def cargar_listado_cliente(request):
    cliente1 = Cliente.objects.all()
    return render(request, "listado_cliente.html", {'clientes': cliente1})

def editar_cliente(request, id):
    cliente1 = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForms(instance=cliente1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_cliente.html", contexto)
    else:
        form = ClienteForms(request.POST, instance=cliente1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_cliente')
    return render(request, "crear_cliente.html", contexto)


def eliminar_cliente(request, id):
    cliente1 = Cliente.objects.get(id=id)
    cliente1.delete()
    return redirect('consulta_cliente')

def cargar_listado_productos(request):
    factura1 = Producto.objects.all()
    return render(request, "listado_producto.html", {'factura': factura1})


def crear_producto(request):
    if request.method == 'GET':
        formulario = ProductoForms()
        contexto = {
            'formulario': formulario
        }
        return render(request, "crear_producto.html", contexto)
    else:
        formulario = ProductoForms(request.POST)
        contexto = {
            'form': formulario
        }
        # print(formulario)
        if formulario.is_valid():
            formulario.save()
        return redirect('consulta_producto')


def eliminar_producto(request, id):
    articulo1 = Producto.objects.get(id=id)
    articulo1.delete()
    return redirect('consulta_producto')


def editar_producto(request, id):
    articulo1 = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForms(instance=articulo1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_producto.html", contexto)
    else:
        form = ProductoForms(request.POST, instance=articulo1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_producto')
    return render(request, "crear_producto.html", contexto)


def buscar_usuario(request):
    usuario = request.GET['usuario']
    clave = request.GET['clave']

    if (usuario=="" and  clave==""):
      cadena= "No ingreso los datos a consultar"
      return HttpResponse(cadena)
    else:
      data= Cliente.objects.filter(nombres=usuario, apellido=clave)
      return render(request, "Dashboard.html", {"datos": data, "usuario": usuario})

def cargar_index(request):
    return render(request, "index.html")

####Prueba

def cargar_listado_factura(request):
    factura1 = Factura.objects.all()
    return render(request, "listado_factura.html", {'facturas': factura1})

def crear_factura(request):
    if request.method == 'GET':
        formulario = FacturaForms()
        contexto = {
            'formulario': formulario
        }
        return render(request, "crear_factura.html", contexto)
    else:
        formulario = FacturaForms(request.POST)
        contexto = {
            'form': formulario
        }
        # print(formulario)
        if formulario.is_valid():
            formulario.save()
        return redirect('consulta_factura')

def eliminar_factura(request, id):
    articulo1 = Factura.objects.get(id=id)
    articulo1.delete()
    return redirect('consulta_factura')

def editar_factura(request, id):
    articulo1 = Factura.objects.get(id=id)
    if request.method == 'GET':
        form = FacturaForms(instance=articulo1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_factura.html", contexto)
    else:
        form = FacturaForms(request.POST, instance=articulo1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_factura')
    return render(request, "crear_factura.html", contexto)

def mivista1():
    return "hola mundo"

def mivista2():
    return "hola mundo"

#Detalle factura xd

def cargar_listado_detalle(request):
    detalle1 = Detalle_factura.objects.all()
    return render(request, "listado_detalle.html", {'detalle': detalle1})

def crear_detalle(request):
    if request.method == 'GET':
        formulario = DetalleForms()
        contexto = {
            'formulario': formulario
        }
        return render(request, "crear_detalle.html", contexto)
    else:
        formulario = DetalleForms(request.POST)
        contexto = {
            'form': formulario
        }
        # print(formulario)
        if formulario.is_valid():
            formulario.save()
        return redirect('consulta_detalle')

def eliminar_detalle(request, id):
    articulo1 = Detalle_factura.objects.get(id=id)
    articulo1.delete()
    return redirect('consulta_detalle')

def editar_detalle(request, id):
    articulo1 = Detalle_factura.objects.get(id=id)
    if request.method == 'GET':
        form = DetalleForms(instance=articulo1)
        contexto = {
                       'formulario': form
                       }
        return render(request, "crear_detalle.html", contexto)
    else:
        form = DetalleForms(request.POST, instance=articulo1)
        contexto = {
            'formulario': form
        }
        if form.is_valid():
            form.save()
            return redirect('consulta_detalle')
    return render(request, "crear_detalle.html", contexto)


