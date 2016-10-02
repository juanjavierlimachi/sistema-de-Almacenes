from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	
	url(r'^newCategoria/$',newCategoria),
	
	url(r'^verCategoria/$',verCategoria),
	url(r'^NewProducto/$',NewProducto),
	
	url(r'^VerProductos/$',VerProductos),
	
	url(r'^addProducto/(?P<id>\d+)/$',addProducto),
	url(r'^deleteCate/(?P<id>\d+)/$',deleteCate),
	url(r'^delCate/(?P<id>\d+)/$',delCate),
	url(r'^editCate/(?P<id>\d+)/$',editCate),

	url(r'^deleteProducto/(?P<id>\d+)/$',deleteProducto),
	url(r'^delProducto/(?P<id>\d+)/$',delProducto),
	url(r'^editProducto/(?P<id>\d+)/$',editProducto),
	url(r'^addCompra/(?P<id>\d+)/$',addCompra),
	url(r'^IngresaProducto/$',IngresaProducto),

	url(r'^Ingresos/(?P<id>\d+)/$',Ingresos),
	url(r'^por_categorias/(?P<id>\d+)/$',por_categorias),
	url(r'^stock_de_productos/(?P<id>\d+)/$',stock_de_productos),
	#urls de Salidas 
	url(r'^salidas/(?P<id>\d+)/$',salidas),
	url(r'^BuscarTrab/$',BuscarTrab),
	url(r'^SalidaProducto/$',SalidaProducto),
	url(r'^SalidaProductoCliente/$',SalidaProductoCliente),
	
	url(r'^get_retorna_salidas/$',get_retorna_salidas),
	#urls de Ingresos
	url(r'^IngresosP/(?P<id>\d+)/$',IngresosP),
	url(r'^BuscarProveedor/$',BuscarProveedor),
	url(r'^IngresosProductos/$',IngresosProductos),
	url(r'^IngresoProductoCliente/$',IngresoProductoCliente),
	url(r'^get_retorna_ingresos/$',get_retorna_ingresos),

	url(r'^uploadFiles/$',uploadFiles),
	url(r'^kardex/(?P<id>\d+)/$',kardex),

	url(r'^inProduct/$',inProduct),
	url(r'^outProduct/$',outProduct),

	url(r'^deleteSalidas/(?P<id>\d+)/$',deleteSalidas),
	url(r'^deleteSalidasConfir/(?P<id>\d+)/$',deleteSalidasConfir),
	url(r'^deleteIngresos/(?P<id>\d+)/$',deleteIngresos),
	url(r'^deleteIngresosConfir/(?P<id>\d+)/$',deleteIngresosConfir),
	url(r'^editIngresos/(?P<id>\d+)/$',editIngresos),
	url(r'^editSalidas/(?P<id>\d+)/$',editSalidas),
	url(r'^buscarProducto_view/$',buscarProducto_view),
	url(r'^ShearProduc/(?P<id>\d+)/$',ShearProduc),

	url(r'^deleteProductoRecuperar/(?P<id>\d+)/$',deleteProductoRecuperar),
	url(r'^capturaImg/$',capturaImg),
	url(r'^captura_qr/$',captura_qr),
	#url(r'^ImprimirKardex/(?P<id>\d+)/$',ImprimirKardex),
	url(r'^detaleProducto/$',detaleProducto),
	
	url(r'^ImprimirKardex/(?P<id>\d+)/$',ImprimirKardex),
	url(r'^update_session/$',update_session),

	url(r'^cantidadSalida/$',CantidadSalida),
	url(r'^cantidadIngresos/$',CantidadIngresos),

)