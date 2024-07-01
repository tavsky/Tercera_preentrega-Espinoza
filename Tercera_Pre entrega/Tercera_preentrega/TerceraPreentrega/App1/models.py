from django.db import models

# Create your models here.
class IngresoStock(models.Model):
    SKU=models.CharField(max_length=50)
    Cantidad=models.Value
    Nombre_encargado=models.CharField(max_length=50)

class cliente(models.Model):
    Nombre=models.CharField(max_length=40)
    email=models.EmailField()
    direccion=models.CharField(max_length=70)
    Fecha_Nacimiento=models.DateField()

class Empleado(models.Model):
    Nombre=models.CharField(max_length=50)
    CARGO_CHOICES = [(1, 'Vendedor'),(2, 'Encargado de tienda'),(3, 'Gerente Zona')]
    Cargo=models.CharField(max_length=50, choices=CARGO_CHOICES)      