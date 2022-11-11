from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class Index(TemplateView):
	template_name = 'login/login.html'

class listadoUsers(ListView):
	template_name = 'login/users.html'
	queryset = ['Uno','Dos'='2','Tres','Cuatro']
	context_object_name = 'lista'
