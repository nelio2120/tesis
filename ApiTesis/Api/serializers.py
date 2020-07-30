from rest_framework import serializers
from .models import *


class PersonasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = '__all__'
		
class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ('idUsuario','nombre','correo','idPersona','correo')

class HistorialUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historial_Usuario
		fields = ('idHistoUsuario','idUsuario','lat','lon','fecha','estado')


class AccesoUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Acceso_Usuario
		fields = "__all__"
