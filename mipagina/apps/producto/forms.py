#encoding:utf-8
from django import forms
from django.forms import ModelForm
from .models import *

tipo = (('Artículo', 'Artículos',), ('Insumo', 'Insumos',),('Desechable', 'Desechables',))
class FormCategoria(ModelForm):
	Material=forms.ChoiceField(widget=forms.Select, choices=tipo)
	class Meta:
		model = Categoria
		exclude=('estado',)

class FormProducto(ModelForm):
	class Meta:
		model = Producto
		exclude=('Usuario','estado','Stock',)

class FormCompra(ModelForm):
	class Meta:
		model=CompraProducto
		exclude=('total','estado',)

class FormSalidas(ModelForm):
	class Meta:
		model=SalidasPro
		exclude=('total','estado',)