from django import forms

class ClienteForm(forms.Form):
    Nombre=forms.CharField(max_length=40,required=True)
    email=forms.EmailField(required=True)
    Direccion=forms.CharField(max_length=70,required=True)
    Fecha_Nacimiento=forms.DateField()

class EmpleadosForm(forms.Form):
    Nombre=forms.CharField(max_length=40,required=True)
    Cargo=forms.ChoiceField(choices=[('Vendedor', 'Vendedor'),('Encargado de tienda', 'Encargado de tienda'),('Gerente Zona', 'Gerente Zona')], required=True) 


class StockForm(forms.Form):
    SKU=forms.CharField(max_length=50)
    Cantidad=forms.CharField(max_length=50)
    Nombre_encargado=forms.CharField(max_length=50)
    Nombre_Producto=forms.CharField(max_length=80)
class VentaForm(forms.Form):
    SKU=forms.CharField(max_length=50)
    Cantidad=forms.CharField(max_length=50)
    Nombre_encargado=forms.CharField(max_length=50)
    Precio=forms.CharField(max_length=50)
    Cliente=forms.CharField(max_length=50)