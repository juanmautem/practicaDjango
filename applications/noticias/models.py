from django.db import models
from applications.usuarios.models import *
# Create your models here.




class noticia(models.Model):
	txtNotice = models.TextField('Texto de Noticia')
	eIdUser = models.ForeignKey(usuario, on_delete=models.CASCADE)
	bActive = models.BooleanField('Activo', default = False)
	fhCreatedAt = models.DateTimeField('Fecha y Hora')
	
	class Meta:
		verbose_name = 'Noticia'
		verbose_name_plural = 'Lista de Noticias'


	def __str__(self):
		return str(self.id) + "-" + self.txtNotice

class picture(models.Model):
	txtName = models.CharField('Nombre Img', max_length = 100)
	txtUrl = models.CharField('URL', max_length = 100)
	eIDNotice = models.ForeignKey(noticia, on_delete=models.CASCADE)
	fhCreatedAt = models.DateTimeField('Fecha y Hora')

	class Meta:
		verbose_name = 'Imagen'
		verbose_name_plural = 'Lista de Imágenes'


	def __str__(self):
		return str(self.id) + "-" + self.txtName