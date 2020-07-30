from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers



router = routers.SimpleRouter()
router.register('listar_usuarios',listar_usuarios)
router.register('acceso_usuario',acceso_usuario)

urlpatterns = [
	path('Listar_persona/',Listar_persona.as_view(),name='Listar_persona'),
]
urlpatterns += router.urls
