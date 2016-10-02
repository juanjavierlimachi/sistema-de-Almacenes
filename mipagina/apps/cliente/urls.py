from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	
	url(r'^NewClient/$',NewClient),
	url(r'^VerClientes/$',VerClientes),
	url(r'^buscar/$',buscar),
	url(r'^deleteTrabajador/(?P<id>\d+)/$',deleteTrabajador),
	url(r'^delTrabajador/(?P<id>\d+)/$',delTrabajador),
	url(r'^editTrabajador/(?P<id>\d+)/$',editTrabajador),

	url(r'^escogido/(?P<id>\d+)/$',escogido),
	url(r'^deleteSalidasRecuperar/(?P<id>\d+)/$',deleteSalidasRecuperar),
)