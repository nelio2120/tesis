from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers



router = routers.SimpleRouter()
router.register('Listar_usuarios',Listar_usuarios)
router.register('Acceso_usuario',Acceso_usuario)
router.register('Contacto_confianza',Contacto_confianza)
router.register('Historial_usuario',Historial_usuario)

urlpatterns = [
	path('Listar_persona/',Listar_persona.as_view(),name='Listar_persona'),
]
urlpatterns += router.urls
