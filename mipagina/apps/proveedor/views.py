#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
from .models import *
from .forms import *
# Create your views here.
def NewProveedor(request):
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormProveedor()
	return render_to_response('proveedor/NewProveedor.html',{'forms':forms},context_instance=RequestContext(request))

def VerPrveedor(request):
	datos=Proveedor.objects.all().order_by('-id')
	return render_to_response('proveedor/VerPrveedor.html',{'datos':datos},context_instance=RequestContext(request))

def deleteProveedor(request, id):
	dato=Proveedor.objects.get(id=int(id))
	return render_to_response('proveedor/deleteProveedor.html',{'dato':dato},context_instance=RequestContext(request))
def delProveedor(request, id):
	Proveedor.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó el Proveedor Correctamente.")

def editProveedor(request, id):
	cod=int(id)
	dato=Proveedor.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormProveedor(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El proveedor se Actualizó Correctamente.")
	else:
		forms=FormProveedor(instance=dato)
	return render_to_response('proveedor/editProveedor.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))

def buscarPro(request):
	if request.method=='POST':
		pass
	else:
		texto=request.GET["q"]
		busqueda=(
				Q(Nombre_Razon_Social__icontains=texto) |
				Q(Nit__icontains=texto) |
				Q(Telefono__icontains=texto)
			)
		resultados=Proveedor.objects.filter(busqueda).distinct()
	return render_to_response('proveedor/buscarPro.html',{'resultados':resultados},context_instance=RequestContext(request))

