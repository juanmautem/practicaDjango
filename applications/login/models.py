from django.db import models
import hashlib

# Create your models here.

class userPass(models.Model):
	#campos
	user = models.CharField(max_length = 15)
	password = models.CharField(max_length = 32)
	def __str__(self):
		return "Id: "+ str(self.id) + "| UserName= " + self.user 

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTABLE'),
        ('1', 'GERENTE'),
        ('2', 'ADMINISTRATIVO'),
        ('3', 'RECURSOS HUMANOS'),
        ('4', 'OTROS'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellidos', max_length=120)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name