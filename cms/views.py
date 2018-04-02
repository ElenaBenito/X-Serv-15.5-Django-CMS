from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages
# Create your views here.

def pagina_inicial(request):
	respuesta = "Página inicial. Estos son los recursos que hay:"
	paginas = Pages.objects.all()
	for pagina in paginas:
		respuesta += '<br><a href="/recurso/' + str(pagina.id) + '">' + pagina.name + '</a>'

	return HttpResponse(respuesta)

def pagina(request,identificador):
	try:
		pagina = Pages.objects.get(id = identificador)
		respuesta = "Has introducido " + str(pagina.id) + ", recurso que corresponde a '" + str(pagina.page) + "' y su id es: " + str(pagina.id)
	
	except Pages.DoesNotExist:
		respuesta = "No existe la página con el identificador " + str(identificador)

	return HttpResponse(respuesta)
