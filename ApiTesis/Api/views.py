from rest_framework import viewsets
from .models import *
from .serializers import *
import hashlib
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import datetime 
from django.shortcuts import render

# Create your views here.


class Listar_roles(viewsets.ModelViewSet):
	serializer_class = RolesSerializer
	queryset = Roles.objects.filter()

class Historial_usuario(viewsets.ModelViewSet):
	serializer_class = HistorialUsuarioSerializer
	queryset = Historial_Usuario.objects.all()

	def get_queryset(self):
		if not self.request.query_params.get('idUsuario'):
			queryset = Historial_Usuario.objects.all() 
			return queryset
		else:
			idUsuario = self.request.query_params.get('idUsuario')
			queryset = Historial_Usuario.objects.get(idUsuario=idUsuario)
			return queryset

class Contacto_confianza(viewsets.ModelViewSet):
	serializer_class = ContactoConfianzaSerializer
	queryset = Contacto_confian.objects.all()


class Acceso_usuario(viewsets.ModelViewSet):
	serializer_class = AccesoUsuarioSerializer
	queryset = Acceso_Usuario.objects.filter()

	def get_queryset(self):
		if not self.request.query_params.get('idUsuario'):
			queryset = Acceso_Usuario.objects.all()
			return queryset
		else:
			id_usuario = self.request.query_params.get('idUsuario')
			queryset = Acceso_Usuario.objects.filter(idUsuario=id_usuario)
			return queryset


class Listar_Usuario(APIView):
	def get(self, request, *args, **kwargs):
		if not request.query_params.get('usuario') and not request.query_params.get('password'):
			lista_usuario = Usuario.objects.filter(estado='A')
			serializer = UsuarioSerializer(lista_usuario,many=True)
			return Response(data=serializer.data, status=status.HTTP_200_OK)
		else:
			lista_usuario = Usuario.objects.filter(estado='A',nombre=request.query_params.get('usuario'),password=request.query_params.get('password'))
			serializer = UsuarioSerializer(lista_usuario,many=True)
			return Response(data=serializer.data, status=status.HTTP_200_OK)
	
	def post(self, request):
	 	serializer = UsuarioSerializer(data=request.data)
	 	try:
	 		if serializer.is_valid():
	 			serializer.save()
	 			return Response(data=serializer.data, status=status.HTTP_200_OK)
	 		else:
	 			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	 	except Exception as e:
	 		print(e)
	 		return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request):
		persona = Usuario.objects.get(idUsuario=request.data['idUsuario'])
		serializer = UsuarioSerializer(persona, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Listar_persona(APIView):
	
	def get(self, request):
	 	if not request.query_params.get('idPersona'):
	 		lista_personas = Persona.objects.filter(estado='A')
	 		serializer = PersonasSerializer(lista_personas, many=True)
	 		return Response(data=serializer.data, status=status.HTTP_200_OK)
	 	else:
	 		persona = Persona.objects.get(idPersona=request.query_params.get('idPersona'))
	 		serializer = PersonasSerializer(persona, many=False)
	 		return Response(data=serializer.data, status=status.HTTP_200_OK)
	
	def post(self, request):
	 	serializer = PersonasSerializer(data=request.data)
	 	try:
	 		if serializer.is_valid():
	 			serializer.save()
	 			return Response(data=serializer.data, status=status.HTTP_200_OK)
	 		else:
	 			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	 	except Exception as e:
	 		print(e)
	 		return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request):
		persona = Persona.objects.get(idPersona=request.data['idPersona'])
		serializer = PersonasSerializer(persona, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request):
		persona = Persona.objects.get(idPersona=request.query_params.get('idPersona'))
		persona.delete()
		return Response(data={"elemento eliminado": "Eliminado completo"}, status=status.HTTP_202_ACCEPTED)


