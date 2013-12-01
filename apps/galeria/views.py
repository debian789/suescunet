from django.shortcuts import render_to_response,render #arma el contenido 
from django.template import RequestContext # permite incluir el contexto
from models import galeria_model # modelos
from forms import addGaleriaForms,addGaleriaForms2 # Formularios
from django.http import HttpResponseRedirect #Redireccionar
from django.core.paginator import Paginator,EmptyPage,InvalidPage #pagina d

######## formularios  ###############

def add_galerias_view1(request):
	info = "Inicializado"		
	if request.user.is_authenticated():

		if request.method == "POST":
			formulario = addGaleriaForms2(request.POST,request.FILES) #FILES agrega los archivos gargados
			if formulario.is_valid():

				titulo = formulario.cleaned_data['titulo']
				contenido = formulario.cleaned_data['contenido']
				publicado = formulario.cleaned_data['publicado']
				imagen = formulario.cleaned_data['imagen'] 

				galeria= galeria_model()
				galeria.titulo = titulo
				galeria.contenido = contenido
				galeria.publicado = publicado 
				if imagen:
					galeria.imagen = imagen 

				galeria.save()

				#formulario.save()
			return HttpResponseRedirect('/galeria/')

		else:

			formulario = addGaleriaForms2()
			contexto = {"formulario":formulario}
			return render("galeria_ingresar.html",contexto)
	else:
		return HttpResponseRedirect("/")



def add_galerias_view2(request):
	if request.user.is_authenticated():

		if request.method == "POST":
			contenidoForm = addGaleriaForms(request.POST,request.FILES)
			if contenidoForm.is_valid :
				contenidoForm.save()
				return HttpResponseRedirect('/galeria/')

		
		formulario = addGaleriaForms()
		contexto = {'formulario':formulario}

		return render(request,'galeria_ingresar.html',contexto)
	else:
		return HttpResponseRedirect("/")

######### fin de formularios #############
#### vistas ########


def galeria_view(request):
	galerias = galeria_model.objects.filter(publicado=True)
	contexto =  {"galerias":galerias}
	return render(request,"galeria.html",contexto)


def single_galeria_view(request,id_galeria):
	galeria = galeria_model.objects.get(id=id_galeria)
	contexto = {'galerias':galeria}
	return render(request,'galeria_detalle.html',contexto)




#	return render_to_response("galerias/galerias.html",context_instance=RequestContext(request))	
