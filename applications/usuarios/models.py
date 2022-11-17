from django.db import models
from applications.personas.models import persona
# Create your models here.

class usuario(models.Model):
	user_types = (
		('0', 'ADMINISTRADOR DEL SISTEMA'),
        ('1', 'GERENTE'),
        ('2', 'ADMINISTRATIVO'),
        ('3', 'RECURSOS HUMANOS'),
        ('4', 'VISITANTE'),
	)

	eIdPersona = models.ForeignKey(persona, on_delete=models.CASCADE)
	txtUser = models.CharField('NickName',max_length = 30)
	txtPass = models.CharField('Password',max_length = 60)
	txtUserType = models.CharField('Tipo de Usuario', max_length=1, choices=user_types)
	fhCreatedAt = models.DateTimeField('Fecha y Hora')
	bActive = models.BooleanField('Activo',default = False)

	def __str__(self):
		return str(self.id) + "-" + self.txtUser

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Lista de Usuarios'
