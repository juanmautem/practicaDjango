from django.contrib import admin
from .models import *
# Register your models here.


class noticiaAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'txtNotice',
		'eIdUser',
		'bActive',
		'fhCreatedAt',
	)

class pictureAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'txtName',
		'txtUrl',
		'eIDNotice',
		'fhCreatedAt',
	)

admin.site.register(noticia,noticiaAdmin)
admin.site.register(picture, pictureAdmin)
