from django.db import models

def url(self,filename):
	ruta ="MultimediaData/productos/%s"% filename
	return ruta 


class enlacesExterno_model(models.Model):
	titulo      = models.CharField(max_length = 300)
	url         = models.URLField(max_length = 200)
	imagen 		= models.ImageField(upload_to=url,null=True,blank=True)
	publicado 	= models.BooleanField(default=True)
	descripcion = models.TextField() 

	class Meta:
		verbose_name = ('Enlace')
		verbose_name_plural= ('Enlaces')

	def __unicode__(self):
		return self.titulo



# Create your models here.
