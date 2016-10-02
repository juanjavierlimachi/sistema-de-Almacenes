from django import forms
from django.forms import ModelForm
from .models import *

class FormTrabajador(ModelForm):
	class Meta():
		model = Trabajador
		exclude=('estado',)