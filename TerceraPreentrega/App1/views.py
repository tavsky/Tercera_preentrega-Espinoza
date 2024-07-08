from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.

def home(request):
    return render(request, "App1/index.html")

def Empleados(request):
    contexto={"Empleados":Empleado.objects.all() }
    return render(request, "App1/Empleados.html",contexto)

def Stock(request):
    contexto={"Stock":IngresoStock.objects.all() }
    return render(request, "App1/Stock.html", contexto)

def Clientes(request):
    contexto={"Clientes":Cliente.objects.all() }
    return render(request, "App1/Clientes.html", contexto)

def Ventas(request):
    contexto={"Ventas":IngresoVenta.objects.all() }
    return render(request, "App1/Ventas.html", contexto)

# Formularios

def ClientesForm(request):
    if request.method == "POST":
        FormularioCliente=ClienteForm(request.POST)
        if FormularioCliente.is_valid():
            Cliente_Nombre=FormularioCliente.cleaned_data.get("Nombre")
            Cliente_Email=FormularioCliente.cleaned_data.get("email")
            Cliente_Direccion=FormularioCliente.cleaned_data.get("Direccion")
            Cliente_Fecha_Nacimiento=FormularioCliente.cleaned_data.get("Fecha_Nacimiento")        
            cliente=Cliente(Nombre=Cliente_Nombre, email=Cliente_Email,direccion=Cliente_Direccion,Fecha_Nacimiento=Cliente_Fecha_Nacimiento)
            cliente.save()
            contexto={"Clientes": Cliente.objects.all() }
            return render(request, "App1/Clientes.html", contexto)
    
    else:
        FormularioCliente = ClienteForm()

    return render (request,"App1/ClientesForm.html", {"form":FormularioCliente})

def EmpleadoForm(request):
    if request.method == "POST":
        FormularioEmpleado=EmpleadosForm(request.POST)
        if FormularioEmpleado.is_valid():
            Empleado_Nombre=FormularioEmpleado.cleaned_data.get("Nombre")
            Empleado_Cargo=FormularioEmpleado.cleaned_data.get("Cargo")    
            empleado=Empleado(Nombre=Empleado_Nombre, Cargo=Empleado_Cargo)
            empleado.save()
            contexto={"Empleados": Empleado.objects.all() }
            return render(request, "App1/Empleados.html", contexto)
    
    else:
        FormularioEmpleado = EmpleadosForm()

    return render (request,"App1/EmpleadosForm.html", {"form":FormularioEmpleado})

def stockForm(request):
    if request.method == "POST":
        FormularioStock=StockForm(request.POST)
        if FormularioStock.is_valid():
            Stock_SKU=FormularioStock.cleaned_data.get("SKU")
            Stock_Cantidad=FormularioStock.cleaned_data.get("Cantidad")
            Stock_Nombre_encargado=FormularioStock.cleaned_data.get("Nombre_encargado")      
            Stock_Nombre_Producto=  FormularioStock.cleaned_data.get("Nombre_Producto")  
            stock=IngresoStock(SKU=Stock_SKU, Cantidad=Stock_Cantidad,Nombre_encargado=Stock_Nombre_encargado,Nombre_Producto=Stock_Nombre_Producto)
            stock.save()
            contexto={"Stock": IngresoStock.objects.all() }
            return render(request, "App1/Stock.html", contexto)
    
    else:
        FormularioStock = StockForm()

    return render (request,"App1/StockForm.html", {"form":FormularioStock})

def VentasForm(request):
    if request.method == "POST":
        FormularioVentas=VentaForm(request.POST)
        if FormularioVentas.is_valid():
            Ventas_SKU=FormularioVentas.cleaned_data.get("SKU")
            Ventas_Cantidad=FormularioVentas.cleaned_data.get("Cantidad")
            Ventas_Nombre_encargado=FormularioVentas.cleaned_data.get("Nombre_encargado")   
            Ventas_Precio=FormularioVentas.cleaned_data.get("Precio")   
            Ventas_Cliente=FormularioVentas.cleaned_data.get("Cliente")     
            venta=IngresoVenta(SKU=Ventas_SKU, Cantidad=Ventas_Cantidad,Nombre_encargado=Ventas_Nombre_encargado,Precio=Ventas_Precio,Cliente=Ventas_Cliente)
            venta.save()
            contexto={"Ventas": IngresoVenta.objects.all() }
            return render(request, "App1/Ventas.html", contexto)
    
    else:
        FormularioVentas = VentaForm()

    return render (request,"App1/VentasForm.html", {"form":FormularioVentas})

#Busquedas

def BuscarStock(request):
    return render(request, "App1/BuscarStock.html")

def EncontrarStock(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        Stock=IngresoStock.objects.filter(SKU=patron)
        contexto={'Stock':Stock}
    else:
        contexto={'Stock':IngresoStock.objects.all()}
    return render(request, "App1/Stock.html", contexto)