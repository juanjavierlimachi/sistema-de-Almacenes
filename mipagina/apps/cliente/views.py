#encoding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from mipagina.apps.producto.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from django.db.models import Q
from .forms import *
import datetime
import calendar
# Create your views here.
def NewClient(request):
	if request.method=='POST':
		forms=FormTrabajador(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormTrabajador()
	return render_to_response('cliente/NewClient.html',{'forms':forms},context_instance=RequestContext(request))

def VerClientes(request):
    datos=Trabajador.objects.all().order_by('-id')
    cliente=Trabajador.objects.filter(estado=0).count()
    return render_to_response('cliente/VerClientes.html',{'datos':datos,'cliente':cliente},context_instance=RequestContext(request))

def buscar(request):
    if request.method=="POST":
        #"""Aqui ira otra busqueda igual que abajo"""
        #return HttpResponse("hecho")
        texto=request.POST["q"]
        busqueda=(
            Q(Nombre_trabajador__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Trabajador.objects.filter(busqueda).distinct()
        print "Clente:",resultados
        return render_to_response('cliente/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

    else:
        texto=request.GET["q"]
        busqueda=(
            Q(Nombre_trabajador__icontains=texto) |
            Q(Apellidos__icontains=texto) |
            Q(Ci_Nit__icontains=texto)
        )
        resultados=Trabajador.objects.filter(busqueda).distinct()
        # html="<ul class='ul_lista'>"
        # for i in resultados:
        #     html=html+"<li><a href='/detalles/"+str(i.id)+"/'>"+i.Nombre_trabajador+""+i.Apellidos+"</a></li>"
        # html=html+"<ul>"
        return render_to_response('cliente/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

def deleteTrabajador(request, id):
    dato=Trabajador.objects.get(id=int(id))
    return render_to_response('cliente/deleteTrabajador.html',{'dato':dato},context_instance=RequestContext(request))
def delTrabajador(request, id):
    Trabajador.objects.filter(id=int(id)).update(estado=1)
    return HttpResponse("Se eliminó el registro correctamente.")
def editTrabajador(request, id):
    cod=int(id)
    dato=Trabajador.objects.get(id=int(id))
    if request.method=='POST':
        forms=FormTrabajador(request.POST, instance=dato)
        if forms.is_valid():
            forms.save()
            return HttpResponse("El registro se actualizó correctamente")
    else:
        forms=FormTrabajador(instance=dato)
    return render_to_response('cliente/editTrabajador.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
  
def escogido(request,id):
    persona=Trabajador.objects.get(id=int(id))
    fecha=datetime.datetime.now()
    dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
    #la linea de abajo Consultamos todas las selidas q el cliente realizo con el MES 
    ventas=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart).order_by("-id")
    #cont=SalidasPro.objects.filter(trabajador=int(id),estado=0).count()
    cont=SalidasPro.objects.filter(trabajador=int(id), fecha_registro__gte=dateMonthStart).count()
    dic={
        'ventas':ventas,
        'cont':cont,
        'persona':persona
    }
    return render_to_response('cliente/escogido.html',dic,context_instance=RequestContext(request))
def deleteSalidasRecuperar(request, id):
    SalidasPro.objects.filter(id=int(id)).update(estado=0)
    return HttpResponse("El registro a sido Activado.")