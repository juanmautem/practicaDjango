from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import userPass

class Index(TemplateView):
	template_name = 'login/login.html'

class listadoUsers(ListView):
	template_name = 'login/users.html'
	queryset = ['Uno','Dos','Tres','Cuatro']
	context_object_name = 'lista'

class listadoUsers2(ListView):
	template_name = 'login/users.html'
	model = userPass
	context_object_name = 'lista'


