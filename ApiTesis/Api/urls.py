from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers



router = routers.SimpleRouter()
router.register('Acceso_usuario',Acceso_usuario)
router.register('Contacto_confianza',Contacto_confianza)
router.register('Historial_usuario',Historial_usuario)
router.register('Roles',Listar_roles)

urlpatterns = [
	path('Listar_persona/',Listar_persona.as_view(),name='Listar_persona'),
	path("Listar_usuario/",Listar_Usuario.as_view(),name='Listar_usuario')
]
urlpatterns += router.urls
