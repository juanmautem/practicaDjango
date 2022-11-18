from django.contrib import admin

from .models import *
# Register your models here.

class usuarioAdmin(admin.ModelAdmin):
	list_display = (
		'eIdPersona',
		'txtUser',
		'txtPass',
		'txtUserType',
		'fhCreatedAt',
		'bActive',
	)

admin.site.register(usuario,usuarioAdmin)
