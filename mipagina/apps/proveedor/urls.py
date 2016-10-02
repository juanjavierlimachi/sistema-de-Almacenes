from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
	
	url(r'^NewProveedor/$',NewProveedor),
	url(r'^VerPrveedor/$',VerPrveedor),

	url(r'^deleteProveedor/(?P<id>\d+)/$',deleteProveedor),
	url(r'^delProveedor/(?P<id>\d+)/$',delProveedor),
	url(r'^editProveedor/(?P<id>\d+)/$',editProveedor),

	url(r'^buscarPro/$',buscarPro),
)