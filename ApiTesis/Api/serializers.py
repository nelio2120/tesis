from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Roles
		fields = '__all__'
		
class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = "__all__"

class HistorialUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historial_Usuario
		fields = ('idHistoUsuario','idUsuario','lat','lon','fecha','estado')


class AccesoUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Acceso_Usuario
		fields = "__all__"

class HistorialUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historial_Usuario
		fields = "__all__"

class ContactoConfianzaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contacto_confian
		fields = "__all__"