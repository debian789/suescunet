from django.shortcuts import render_to_response,get_object_or_404,render
from django.template import RequestContext
from apps.codigos.models import *
from apps.codigos.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,InvalidPage


from django.utils.html import escape
from pygments.lexers import LEXERS

def codigos_view(request):
	if request.method == 'POST':
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		print formularioBusqueda
		codigosBuequeda = mdl_codigos.objects.filter(titulo= formularioBusqueda.cleaned_data['buesqueda'])
		contexto = {"codigos":codigosBuequeda,"formularioBusqueda":formularioBusqueda}
		return render(request,"codigos.html",contexto)
	#contexto = {"codigos":codigos}
	else:
		formularioBusqueda = frm_codigos_busqueda()
		codigos = mdl_codigos.objects.filter(publicado=True)
		contexto = {"codigos":codigos,"formularioBusqueda":formularioBusqueda}
		return render(request,"codigos.html",contexto)
	#return render_to_response("codigos.html",contexto,context_instance = RequestContext(request))




def view_agregar_codigo(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			contenidoForm = frm_codigos(request.POST,request.FILES)
			if contenidoForm.is_valid:
				contenidoForm.save()
				return HttpResponseRedirect('/codigos/1')


		formulario = frm_codigos()
		contexto = {'formulario':formulario}
		#return render_to_response('codigos/codigo_ingresar.html',contexto,context_instance=RequestContext(request))
		return render(request,'codigo_ingresar.html',contexto)
	else:
		return HttpResponseRedirect('/codigos/')



#def view_codigos(request,pagina):
#	codigos = mdl_codigos.objects.filter(publicado=True)
	#lenguaje = mdl_lenguaje.objects.all()
#	contexto = {"codigos":codigos,"formularioBusqueda":formularioBusqueda}
	#return render_to_response("codigos.html",contexto,context_instance = RequestContext(request))
#	return render(request,"codigos.html",contexto)



def single_codigo(request,id_codigo):
	if request.method == 'POST':
		formularioBusqueda = frm_codigos_busqueda(request.POST)
		#print formularioBusqueda
		codigosBuequeda = mdl_codigos.objects.filter(titulo= formularioBusqueda.cleaned_data['buesqueda'])
		contexto = {"codigos":codigosBuequeda,"formularioBusqueda":formularioBusqueda}
		return render(request,"codigos.html",contexto)
	else:
		formularioBusqueda = frm_codigos_busqueda()
		codigo = mdl_codigos.objects.get(id=id_codigo)
		codigoFuente = '<pre lang="'+ escape(codigo.lenguaje) +'">' + escape(codigo.codigo) + '</pre>' 

		contexto = {"codigo":codigo,"formularioBusqueda":formularioBusqueda,"codigoFuente":codigoFuente}
		return render(request,'codigo_detalles.html',contexto)

	#     raw_snippet="""
	# class ListHtmlFormatter(HtmlFormatter):
	#     def wrap(self, source, outfile):
	#         return self._wrap_div(self._wrap_pre(self._wrap_list(source)))

	#     def _wrap_list(self, source):
	#         yield 0, '<ol>'
	#         for i, t in source:
	#             if i == 1:
	#                 # it's a line of formatted code
	#                 t = '<li><div class="line">%s</div></li>' % t
	#             yield i, t
	#         yield 0, '</ol>'
	#     # a unicode co
	#     """
	#     snippet = '<pre lang="python">' + escape(raw_snippet) + '</pre>'
	#     contexto2 = {"datos":snippet}
	#     print(contexto2)
	#     return render(request,'codigo_detalles.html',contexto2)

from django.views.generic import ListView, DetailView


class CodigosListView(ListView):
	model = mdl_codigos
	context_object_name = 'codigos'
	def get_template_names(self):
		return 'codigos.html'

class CodigosDetailView(DetailView):
	model = mdl_codigos
	def get_template_names(self):
		return 'codigos.html'


from apps.codigos.serializers import  codigosSerializer,lenguajeSerializer,soSerializer
from rest_framework import viewsets
from apps.elementos_comunes.models import *


class CodigosViewSet(viewsets.ModelViewSet):
	queryset = mdl_codigos.objects.all()
	serializer_class = codigosSerializer

class LenguajeViewSet(viewsets.ModelViewSet):
	queryset = mdl_lenguaje.objects.all()
	serializer_class = lenguajeSerializer

class SoViewSet(viewsets.ModelViewSet):
	queryset = mdl_sistema_operativo.objects.all()
	serializer_class = soSerializer


