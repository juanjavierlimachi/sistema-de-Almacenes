#encoding:utf-8
from django.shortcuts import render, render_to_response
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import User
from .forms import *
from mipagina.apps.proveedor.models import *
from mipagina.apps.proveedor.forms import *
from django.db.models import Q
from mipagina.apps.cliente.models import *
import json
import datetime
import calendar
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
# Create your views here.
def newCategoria(request):
	if request.method=='POST':
		form=FormCategoria(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("ok")
	else:
		form=FormCategoria()
	return render_to_response('producto/newCategoria.html',{'form':form},context_instance=RequestContext(request))

def verCategoria(request):
	datos=Categoria.objects.all().order_by("-id")
	cont=Categoria.objects.filter(estado=0).count()
	return render_to_response('producto/verCategoria.html',{'datos':datos,'cont':cont}, context_instance=RequestContext(request))
def NewProducto(request):
	if request.method =='POST':
		Usuario=Producto(Usuario=request.user)
		forms=FormProducto(request.POST,request.FILES,instance=Usuario, )
		if forms.is_valid():
			forms.save()
			return HttpResponse("ok")
	else:
		forms=FormProducto()
	return render_to_response('producto/NewProducto.html',{'forms':forms}, context_instance=RequestContext(request))

def VerProductos(request):
	datos=Producto.objects.all().order_by("-id")
	cont=Producto.objects.filter(estado=0).count()
	forms=FormCompra()
	categorias=Categoria.objects.filter(estado=0).order_by('-id')
	
	#print request.session.session_key

	return render_to_response('producto/VerProductos.html',{'datos':datos, 'cont':cont,'forms':forms,'categorias':categorias}, context_instance=RequestContext(request))
def addProducto(request, id):
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Registro Exitoso")
	else:
		forms=FormProveedor()
	return render_to_response('proveedor/NewProveedor.html',{'forms':forms},context_instance=RequestContext(request))

def deleteCate(request, id):
	dato=Categoria.objects.get(id=int(id))
	return render_to_response('producto/deleteCate.html',{'dato':dato},context_instance=RequestContext(request))
def delCate(request, id):
	Categoria.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("La Categoria de eliminó correctamente.")

def editCate(request, id):
	cod=int(id)
	dato=Categoria.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormCategoria(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("La Categoria se Actualizó Correctamente.")
	else:
		forms=FormCategoria(instance=dato)
	return render_to_response('producto/editCate.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))

def deleteProducto(request, id):
	dato=Producto.objects.get(id=int(id))
	return render_to_response('producto/deleteProducto.html',{'dato':dato},context_instance=RequestContext(request))
def delProducto(request, id):
	Producto.objects.filter(id=int(id)).update(estado=1)
	return HttpResponse("Se Eliminó el Producto Correctamente.")
def editProducto(request, id):
	cod=int(id)
	dato=Producto.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormProducto(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El Producto se Actualizó Correctamente.")
	else:
		forms=FormProducto(instance=dato)
	return render_to_response('producto/editProducto.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def addCompra(request, id):
	cod=int(id)
	if request.method=='POST':
		forms=FormProveedor(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El Producto se Actualizó Correctamente.")
	else:
		forms=FormProveedor()
	return render_to_response('producto/addCompra.html',{'cod':cod,'forms':forms},context_instance=RequestContext(request))


def IngresaProducto(request):
	if request.method=='POST':
		forms=FormCompra(request.POST)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Se Registro los datos Carrectamente.")
	else:
		forms=FormCompra()
	return render_to_response('producto/IngresaProducto.html',{'forms':forms},context_instance=RequestContext(request))

def Ingresos(request, id):
	producto=id
	compras=CompraProducto()
	exito=False
	compras.Precio_unidad=request.GET['pre']
	compras.cantidad=request.GET['conta']
	compras.producto_id=producto
	compras.proveedor_id=request.GET['prov']
	compras.save()
	exito=True
	print "Compra realizada"
	if exito==True:
		dato=CompraProducto.objects.all().order_by('-id')[0:1]
		actual=Producto.objects.get(id=int(id))
		actual=actual.Stock+int(request.GET['conta'])
		print "Actual",actual
		Producto.objects.filter(id=int(id)).update(Stock=actual)
		print dato
	return render_to_response('producto/Ingresos.html',{'exito':exito,'dato':dato},context_instance=RequestContext(request))
def por_categorias(request, id):
	datos=Producto.objects.filter(Categoria=int(id)).order_by('-id')
	cont=Producto.objects.filter(Categoria=int(id)).count()
	forms=FormCompra()
	cate=Categoria.objects.get(id=int(id))
	return render_to_response('producto/por_categorias.html',{'datos':datos,'forms':forms,'cont':cont,'cate':cate},context_instance=RequestContext(request))
def stock_de_productos(request, id):
	valor = int(id)
	print "Volar",valor
	if valor == 0 :
		datos=Producto.objects.filter(Stock=int(id)).order_by('-id')
		cont=Producto.objects.filter(Stock=int(id), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 1:
		datos=Producto.objects.filter(Stock__range=(1,9)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(1,9), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 2:
		datos=Producto.objects.filter(Stock__range=(10,24)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(10,24), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 3:
		datos=Producto.objects.filter(Stock__range=(25,59)).order_by('-id')
		cont=Producto.objects.filter(Stock__range=(25,59), estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))
	if valor == 4:
		datos=Producto.objects.filter(Stock__gte=60).order_by('-id')
		cont=Producto.objects.filter(Stock__gte=60, estado=0).count()
		return render_to_response('producto/por_categorias.html',{'datos':datos,'cont':cont},context_instance=RequestContext(request))



def salidas(request, id):
	id_pro=int(id)
	return render_to_response('producto/salidas.html',{'id_pro':id_pro},context_instance=RequestContext(request))
from django.core import serializers
def BuscarTrab(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		id_producto=request.GET['producto']
		print "ESTE ES EL PRODUCTOOOOO",id_producto
		datoProducto=Producto.objects.get(id=int(id_producto))
		busqueda=(
			Q(Nombre_trabajador__icontains=trabajador) |
			Q(Apellidos__icontains=trabajador) |
			Q(Ci_Nit__icontains=trabajador)
		)
		resultados=Trabajador.objects.filter(busqueda).distinct()
		#data = serializers.serialize('json', resultados) dos linas para traer datos en formato JSON
		#return HttpResponse(data,content_type="application/json")
		#return HttpResponse(json.dumps({"data":data}),content_type="application/json")
		return render_to_response('cliente/buscarTrabjador.html',{'resultados':resultados,'datoProducto':datoProducto},context_instance=RequestContext(request))
	else:
		return HttpResponse("No se encontraron coinsidencias")
def SalidaProducto(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		trab=Trabajador.objects.get(id=int(request.GET['trabajador']))
		print 'Estes el el trabajador',trabajador
		#producto=request.GET['producto']
		producto=Producto.objects.get(id=int(request.GET['producto']))
		#forms=FormSalidas()
		#return HttpResponse("Error.")
		return render_to_response('producto/SalidaProducto.html',{'trabajador':trabajador,'producto':producto,'trab':trab},context_instance=RequestContext(request))

def SalidaProductoCliente(request):
	estado=False
	salida=SalidasPro()
	salida.Precio_unidad=float(request.POST['prec'])
	salida.cantidad=int(request.POST['cant'])
	salida.total=float(request.POST['prec'])*float(request.POST['cant'])
	salida.producto_id=int(request.POST['prod'])
	salida.trabajador_id=int(request.POST['trab'])
	total=float(request.POST['prec'])*float(request.POST['cant'])
	estado=True
	if estado == True:
		dato = Producto.objects.get(id=int(request.POST['prod']))
		if dato.Stock >= int(request.POST['cant']) and dato.Stock>0:
			salida.save()
			actual=dato.Stock-int(request.POST['cant'])
			Producto.objects.filter(id=int(request.POST['prod'])).update(Stock=actual)
			ultimoSalida=salida.id
			lista=request.session['carrito']
			lista.append(int(ultimoSalida))
			print lista
			request.session['carrito']=lista
			print "salida",ultimoSalida
			salidas=SalidasPro.objects.get(id=int(ultimoSalida))
			return render_to_response('producto/SalidaProductoCliente.html',{'salidas':salidas,'total':total},context_instance=RequestContext(request))
		else:
			return HttpResponse("El hay suficientes producto para realizar la salida.")
	else:
		return HttpResponse("Error en los datos.")
def get_retorna_salidas(request):
	productos=request.session['carrito']
	salidas=SalidasPro.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				#return render_to_response("producto/get_retorna_salidas.html",{'aux':aux},context_instance=RequestContext(request))
				traba=j.trabajador
				Numcontrol+=str(j.id)+':'
	total_pago=0
	contidadPro=len(out)
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.datetime.now()
	dic={
		'Numcontrol':Numcontrol,
		'fecha':fecha,
		'productos':productos,
		'salidas':salidas,
		'out':out,
		'total_pago':total_pago,
		'traba':traba,
		'contidadPro':contidadPro
	}
	return render_to_response("producto/get_retorna_salidas.html",dic,context_instance=RequestContext(request))
def CantidadSalida(request):
	productos=request.session['carrito']
	contidadPro=len(productos)
	return HttpResponse(contidadPro)
def CantidadIngresos(request):
	productos=request.session['ingreso']
	contidadPro=len(productos)
	return HttpResponse(contidadPro)


def IngresosP(request, id):
	id_pro=int(id)
	return render_to_response('producto/IngresosP.html',{'id_pro':id_pro},context_instance=RequestContext(request)) 

def BuscarProveedor(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		id_producto=request.GET['producto']
		print "ESTE ES EL PRODUCTOOOOO",id_producto
		datoProducto=Producto.objects.get(id=int(id_producto))
		busqueda=(
			Q(Nombre_Razon_Social__icontains=trabajador) |
			Q(Nit__icontains=trabajador) |
			Q(Telefono__icontains=trabajador)
		)
		resultados=Proveedor.objects.filter(busqueda).distinct()
		#data = serializers.serialize('json', resultados) dos linas para traer datos en formato JSON
		#return HttpResponse(data,content_type="application/json")
		#return HttpResponse(json.dumps({"data":data}),content_type="application/json")
		return render_to_response('proveedor/BuscarProveedor.html',{'resultados':resultados,'datoProducto':datoProducto},context_instance=RequestContext(request))
	else:
		return HttpResponse("No se encontraron coinsidencias")

def IngresosProductos(request):
	if request.method=='GET':
		trabajador=request.GET['trabajador']
		trab=Proveedor.objects.get(id=int(request.GET['trabajador']))
		print 'Estes el el trabajador',trabajador
		producto=Producto.objects.get(id=int(request.GET['producto']))
		print 'ID producto',producto
		return render_to_response('producto/IngresosProductos.html',{'trabajador':trabajador,'producto':producto,'trab':trab},context_instance=RequestContext(request))

def IngresoProductoCliente(request):
	estado=False
	salida=CompraProducto()
	salida.Precio_unidad=float(request.POST['prec'])
	salida.cantidad=int(request.POST['cant'])
	salida.producto_id=int(request.POST['prod'])
	salida.proveedor_id=int(request.POST['trab'])
	salida.total=float(request.POST['prec'])*float(request.POST['cant'])
	total=float(request.POST['prec'])*float(request.POST['cant'])
	print "Total a Pagar",total
	estado=True
	if estado == True:
		dato = Producto.objects.get(id=int(request.POST['prod']))
		if int(request.POST['cant']) > 0:
			salida.save()
			actual=dato.Stock+int(request.POST['cant'])
			Producto.objects.filter(id=int(request.POST['prod'])).update(Stock=actual)
			ultimoSalida=salida.id
			print "Ingresooo",ultimoSalida
			lista=request.session['ingreso']
			lista.append(int(ultimoSalida))
			request.session['ingreso']=lista
			salidas=CompraProducto.objects.get(id=int(ultimoSalida))
			return render_to_response('producto/SalidaProductoCliente.html',{'salidas':salidas,'total':total},context_instance=RequestContext(request))
		else:
			return HttpResponse("El hay suficientes producto para realizar la salida.")
	else:
		return HttpResponse("Error en los datos.")

def get_retorna_ingresos(request):
	productos=request.session['ingreso']
	salidas=CompraProducto.objects.all().order_by("-id")
	out=[]
	traba=''
	aux=0
	Numcontrol=''
	for i in productos:
		for j in salidas:
			if i == j.id:
				aux=float(j.cantidad)*float(j.Precio_unidad)
				out.append(aux)
				traba=j.proveedor
				Numcontrol+=str(j.id)+':'
	total_pago=0
	for pago in out:
		total_pago=total_pago+pago
	fecha=datetime.datetime.now()
	user=request.user
	return render_to_response("producto/get_retorna_ingresos.html",{'Numcontrol':Numcontrol,'user':user,'fecha':fecha,'productos':productos,'salidas':salidas,'out':out,'total_pago':total_pago,'traba':traba},context_instance=RequestContext(request))

def uploadFiles(request):
	return render_to_response('producto/uploadFiles.html',{},context_instance=RequestContext(request))

def kardex(request, id):
	producto=Producto.objects.get(id=int(id))
	fecha=datetime.datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(id)).order_by("-id")[0:1]
	dic={
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul
	}
	return render_to_response('producto/kardex.html',dic,context_instance=RequestContext(request))

def inProduct(request):
	fecha=datetime.datetime.now()
	#fecha=fecha.strftime('%Y-%m-%d')
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
	dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month-1)[1])
	print "Incioooo", dateMonthStart
	print "Fecha final", dateMonthEnd
	ingresos=CompraProducto.objects.filter(fecha_registro__range=(dateMonthStart,fecha)).order_by('-id')
	t_ingresos=CompraProducto.objects.filter(fecha_registro__range=(dateMonthStart,fecha),estado=0).count()
	dic={
		'ingresos':ingresos,
		't_ingresos':t_ingresos
	}
	return render_to_response('producto/inProduct.html',dic,context_instance=RequestContext(request))
def outProduct(request):
	fecha=datetime.datetime.now()
	dateMonthStart="%s-%s-01" % (fecha.year, fecha.month)
	dateMonthEnd="%s-%s-%s" % (fecha.year, fecha.month, calendar.monthrange(fecha.year-1, fecha.month-1)[1])
	salidas=SalidasPro.objects.filter(fecha_registro__range=(dateMonthStart,fecha)).order_by('-id')
	t_salidas=SalidasPro.objects.filter(fecha_registro__range=(dateMonthStart,fecha),estado=0).count()
	dic={
		'salidas':salidas,
		't_salidas':t_salidas
	}
	return render_to_response('producto/outProduct.html',dic,context_instance=RequestContext(request))

def deleteSalidas(request, id):
	dato=SalidasPro.objects.get(id=int(id))
	return render_to_response('producto/deleteSalidas.html',{'dato':dato},context_instance=RequestContext(request))

def deleteSalidasConfir(request, id):
	if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
		SalidasPro.objects.filter(id=int(id)).update(estado=1)
		return HttpResponse("En registra a sido Eliminado")
	else:
		return HttpResponse("Ud. no esta autenticado por favor inicie session")

def deleteIngresos(request, id):
	dato=CompraProducto.objects.get(id=int(id))
	return render_to_response('producto/deleteIngresos.html',{'dato':dato},context_instance=RequestContext(request))

def deleteIngresosConfir(request, id):
	if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
		CompraProducto.objects.filter(id=int(id)).update(estado=1)
		return HttpResponse("En registra a sido Eliminado")
	else:
		return HttpResponse("Ud. no esta autenticado por favor inicie session")
def editIngresos(request, id):
	cod=int(id)
	dato=CompraProducto.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormCompra(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Los Datos se actualizaron Correctamente.")
	else:
		forms=FormCompra(instance=dato)
	return render_to_response('producto/editIngresos.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def editSalidas(request, id):
	cod=int(id)
	dato=SalidasPro.objects.get(id=int(id))
	if request.method=='POST':
		forms=FormSalidas(request.POST, instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Los Datos se actualizaron Correctamente.")
	else:
		forms=FormSalidas(instance=dato)
	return render_to_response('producto/editSalidas.html',{'forms':forms,'cod':cod},context_instance=RequestContext(request))
def buscarProducto_view(request):
	if request.method=="POST":
		texto = request.POST['p']
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		print "coinsidencias",resultados
		return render_to_response('producto/buscarProducto_view.html',{'resultados':resultados},context_instance=RequestContext(request))
	else:
		texto=request.GET['p']
		print texto
		busqueda=(
				Q(Nombre_producto__icontains=texto) |
				Q(Marca__icontains=texto) |
				Q(id__icontains=texto)
			)
		resultados=Producto.objects.filter(busqueda).distinct()
		return render_to_response('producto/buscarProducto_view.html',{'resultados':resultados},context_instance=RequestContext(request))
def ShearProduc(request, id):
	producto=Producto.objects.get(id=int(id))
	return render_to_response('producto/ShearProduc.html',{'producto':producto},context_instance=RequestContext(request))

def deleteProductoRecuperar(request, id):
	if request.user.is_authenticated and request.user.is_superuser and request.user.is_active:
		Producto.objects.filter(id=int(id)).update(estado=0)
		return HttpResponse("El Producto a sido recuperato correctamente.")

def capturaImg(request):
	return render(request,'producto/capturaImg.html',context_instance=RequestContext(request))
def captura_qr(request):
	return render(request,'producto/captura_qr.html',context_instance=RequestContext(request))
def detaleProducto(request):
	#id=Producto.objects.all().order_by('-id')[1]
	producto=Producto.objects.latest('id')#optiene el ultimo producto(id) registrado
	fecha=datetime.datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(producto.id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(producto.id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(producto.id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(producto.id)).order_by("-id")[0:1]
	dic={
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul
	}
	return render_to_response('producto/kardex.html',dic,context_instance=RequestContext(request))

def ImprimirKardex(request, id):
	producto=Producto.objects.get(id=int(id))
	fecha=datetime.datetime.now()
	fecha=fecha.strftime('%Y-%m-%d')
	print "Fecha:",fecha
	salidas=SalidasPro.objects.filter(producto=int(id)).count()
	ingresos=CompraProducto.objects.filter(producto=int(id)).count()
	salidas_ul=SalidasPro.objects.filter(producto=int(id)).order_by("-id")[0:1]
	ingresos_ul=CompraProducto.objects.filter(producto=int(id)).order_by("-id")[0:1]
	dic={
		'pagesize':'A4',
		'producto':producto,
		'fecha':fecha,
		'salidas':salidas,
		'ingresos':ingresos,
		'salidas_ul':salidas_ul,
		'ingresos_ul':ingresos_ul
	}
	html = render_to_string('producto/imprimirkardex.html',dic,context_instance=RequestContext(request))
	return generar_pdf(html)


def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),'application/pdf')
	return HttpResponse("Error al generar el reporte")

def update_session(request):
	request.session['carrito']=[]
	request.session['ingreso']=[]
	resp="Se ha Linpiado la Bandeja de Salida"+"<br>"+"Ahora Puedes Realizar Una Nueva"
	return HttpResponse(resp)



