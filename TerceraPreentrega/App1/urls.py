from django.urls import path
from App1 import views
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('Empleados/', Empleados, name="Empleados"),
    path('Ventas/', Ventas, name="Ventas"),
    path('Stock/', Stock, name="Stock"),
    path('Clientes/', Clientes, name="Clientes"),

    #Formularios

    path('ClientesForm/', ClientesForm, name="ClientesForm"),
    path('EmpleadosForm/', EmpleadoForm, name="EmpleadosForm"),
    path('StockForm/', stockForm, name="StockForm"),
    path('VentasForm/', VentasForm, name="VentasForm"),

        #Buscar

    path('BuscarStock/', BuscarStock, name="BuscarStock"),
    path('EncontrarStock/', EncontrarStock, name="EncontrarStock"),


]
