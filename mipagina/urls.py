from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mipagina.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #urls de mi aplicacion inicio
    url(r'^',include("mipagina.apps.inicio.urls")),

    url(r'^',include("mipagina.apps.cliente.urls")),

    url(r'^',include("mipagina.apps.producto.urls")),

    url(r'^',include("mipagina.apps.proveedor.urls")),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
        ),
)
