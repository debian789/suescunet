from models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.template import RequestContext
from django.shortcuts import render_to_response,render


def view_enlaces (request):
	enlaces = enlacesExterno_model.objects.filter(publicado=True)
	contexto = {"enlaces":enlaces}
	return render(request,"enlaces.html",contexto)



# Create your views here.
