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


class listar_usuarios(viewsets.ModelViewSet):
	serializer_class = UsuarioSerializer
	queryset = Usuario.objects.filter()


class acceso_usuario(viewsets.ModelViewSet):
	serializer_class = AccesoUsuarioSerializer
	queryset = Acceso_Usuario.objects.filter()

	def get_queryset(self):
		if not self.request.query_params.get('id_usuario'):
			queryset = Acceso_Usuario.objects.all()
			return queryset
		else:
			id_usuario = self.request.query_params.get('id_usuario')
			queryset = Acceso_Usuario.objects.filter(idUsuario=id_usuario)
			return queryset


class Listar_persona(APIView):
	
	def get(self, request):
	 	if not request.query_params.get('id_persona'):
	 		lista_personas = Persona.objects.filter(estado='A')
	 		serializer = PersonasSerializer(lista_personas, many=True)
	 		return Response(data=serializer.data, status=status.HTTP_200_OK)
	 	else:
	 		persona = Persona.objects.get(id_persona=request.query_params.get('id_persona'))
	 		serializer = PersonasSerializer(persona, many=False)
	 		return Response(data=serializer.data, status=status.HTTP_200_OK)
	
	def post(self, request):
	 	serializer = persona(data=request.data)
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
		persona = Persona.objects.get(id_persona=request.data['id_persona'])
		serializer = PersonasSerializer(nivel, data=request.data)
		if serializer.is_valid():
		    serializer.save()
		    return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request):
		persona = Persona.objects.get(id_persona=request.query_params.get('id_persona'))
		persona.delete()
		return Response(data={"elemento eliminado": "Eliminado completo"}, status=status.HTTP_202_ACCEPTED)


