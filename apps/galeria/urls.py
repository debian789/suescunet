from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('apps.galeria.views',
	url(r'^detalle/galeria/(?P<id_galeria>.*)/$','single_galeria_view', name = 'vista_galeria_detalle'),
	url(r'^add/galeria1/$','add_galerias_view1', name = 'vista_galeria_ingresar1'),
	url(r'^add/galeria2/$','add_galerias_view2', name = 'vista_galeria_ingresar2'),
	url(r'^galeria/$','galeria_view', name = 'galeria'),

)






