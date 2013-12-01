from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from apps.codigos.views import CodigosListView,CodigosDetailView
import settings
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

from rest_framework import routers 
from apps.codigos.views import CodigosViewSet,LenguajeViewSet,SoViewSet

router = routers.DefaultRouter()
router.register(r'links',CodigosViewSet)
router.register(r'lenguaje',LenguajeViewSet)
router.register(r'operativo',SoViewSet)



urlpatterns = patterns('',
    url(r'^',include('apps.proyectos.urls')),
    url(r'^',include('apps.codigos.urls')),
    url(r'^',include('apps.enlacesExternos.urls')),
    url(r'^',include('apps.galeria.urls')),
    url(r'^',include('apps.django_pygments.urls')),


	url(r'^about/$',TemplateView.as_view(template_name='codigos.html'), name='about'),
	#url(r'^codigos2/$',CodigosListView.as_view(), name='codigos2'),
    #url(r'^codigos2/(?P<pk>[\d]+)$',CodigosDetailView.as_view(), name='codigo'),

    url(r'^api/',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{"document_root":settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'suescunet.views.home', name='home'),
    # url(r'^suescunet/', include('suescunet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
