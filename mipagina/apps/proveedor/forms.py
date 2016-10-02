from django import forms
from django.forms import ModelForm
from .models import *

class FormProveedor(ModelForm):
	class Meta():
		model = Proveedor
		exclude=('estado',)