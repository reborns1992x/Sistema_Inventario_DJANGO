from django import forms
from .models import registro_Producto

class registro_Producto_Form(forms.ModelForm):
    class Meta:
        model=registro_Producto
        fields='__all__'