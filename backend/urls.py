from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from monitor.views import SpeciesViewSet, ObservationViewSet, verify_token

# Configura el DefaultRouter y registra los viewsets
router = DefaultRouter()
router.register(r'species', SpeciesViewSet)
router.register(r'observations', ObservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # Incluye todas las rutas generadas por el router
    path('api/v1/verify-token/', verify_token, name='verify-token'),  # Ruta para verificar el token
]
