import datetime
from django import forms
from django.forms import ModelForm
from app_coder.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    code = forms.IntegerField(label='Código')


class UserForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    profession = forms.CharField(max_length=40, label='Profesión')
    phone = forms.CharField(max_length=12, label='Número de contacto')


class TechnologyForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    model = forms.CharField(max_length=30, label='Modelo')


class OrderForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre del Pedido')
    due_date = forms.DateField(
        label='Fecha de Entrega',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    is_delivered = forms.BooleanField(label='Entregado', required=False)
