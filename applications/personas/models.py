from django.db import models

# Create your models here.
class persona(models.Model):
	txtName = models.CharField('Nombre(s)',max_length = 30)
	txtLastName = models.CharField('Apellidos',max_length = 60)
	txtRFC = models.CharField('RFC',max_length = 13, unique = True)
	fhCreatedAt = models.DateTimeField('Fecha y Hora')
	bActive = models.BooleanField('Activo',default = False)

	def __str__(self):
		return str(self.id) + "-" + self.txtRFC

	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'
