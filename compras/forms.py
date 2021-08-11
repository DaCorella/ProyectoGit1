from django import forms
from compras.models import Producto, Cliente, Factura,Detalle_factura

class ClienteForms(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = '__all__'



class ProductoForms(forms.ModelForm):
    class Meta:
        model= Producto
        fields = '__all__'


class FacturaForms(forms.ModelForm):
    class Meta:
        model= Factura
        fields = '__all__'


class DetalleForms(forms.ModelForm):
    class Meta:
        model= Detalle_factura
        fields = '__all__'