#from django import forms
from django.forms import ModelForm
from models import *
from django import forms

class addGaleriaForms(ModelForm):
	class Meta:
		model = galeria_model


class addGaleriaForms2(forms.Form):
	titulo = forms.CharField(max_length = 200)
	contenido = forms.CharField(widget=forms.Textarea)
	publicado = forms.BooleanField(required=True)
	imagen = forms.ImageField(required=False)
	#fecha_publicado = forms.DateField(auto_now = True)