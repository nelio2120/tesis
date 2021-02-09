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
	queryset = Roles.objects.filter(estado='A')

class Historial_usuario(viewsets.ModelViewSet):
	serializer_class = HistorialUsuarioSerializer
	queryset = Historial_Usuario.objects.filter(estado='A')

	def get_queryset(self):
		if not self.request.query_params.get('idUsuario'):
			queryset = Historial_Usuario.objects.filter(estado='A') 
			return queryset
		else:
			id = self.request.query_params.get('idUsuario')
			queryset = Historial_Usuario.objects.filter(idUsuario=id,estado='A')
			return queryset

class Contacto_confianza(viewsets.ModelViewSet):
	serializer_class = ContactoConfianzaSerializer
	queryset = Contacto_confian.objects.filter()


class Acceso_usuario(viewsets.ModelViewSet):
	serializer_class = AccesoUsuarioSerializer
	queryset = Acceso_Usuario.objects.filter()

	def get_queryset(self):
		if not self.request.query_params.get('idUsuario') and not self.request.query_params.get('idHistoUsuario'):
			queryset = Acceso_Usuario.objects.filter()
			return queryset
		elif not self.request.query_params.get('idHistoUsuario'):
			id_usuario = self.request.query_params.get('idUsuario')
			queryset = Acceso_Usuario.objects.filter(idUsuario=id_usuario)
			return queryset
		else:
			id = self.request.query_params.get('idHistoUsuario')
			queryset = Acceso_Usuario.objects.filter(idHistoUsuario=id)
			return queryset


class Listar_Usuario(APIView):
	def get(self, request, *args, **kwargs):
		if not request.query_params.get('usuario') and not request.query_params.get('password'):
			if not request.query_params.get('idUsuario') and not request.query_params.get('nombre') and not request.query_params.get('correo'):
				lista_usuario = Usuario.objects.filter(estado='A')
				serializer = UsuarioSerializer(lista_usuario,many=True)
				return Response(data=serializer.data, status=status.HTTP_200_OK)
			elif request.query_params.get('nombre'):
				lista_usuario = Usuario.objects.filter(nombre=request.query_params.get('nombre'),estado='A')
				serializer = UsuarioSerializer(lista_usuario,many=True)
				return Response(data=serializer.data, status=status.HTTP_200_OK)
			elif request.query_params.get('correo'):
				lista_usuario = Usuario.objects.filter(correo=request.query_params.get('correo'),estado='A')
				serializer = UsuarioSerializer(lista_usuario,many=True)
				return Response(data=serializer.data[0], status=status.HTTP_200_OK)
			else:
				lista_usuario = Usuario.objects.filter(idUsuario=request.query_params.get('idUsuario'),estado='A')
				serializer = UsuarioSerializer(lista_usuario,many=True)
				return Response(data=serializer.data[0], status=status.HTTP_200_OK)
				
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
	
		

