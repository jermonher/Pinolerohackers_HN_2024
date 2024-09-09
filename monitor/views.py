from django.http import JsonResponse
from firebase_admin import auth as firebase_auth
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .models import Species, Observation
from .serializers import SpeciesSerializer, ObservationSerializer
from .firebase_admin_setup import *  # Asegúrate de que Firebase esté inicializado

# Verificación del token de Firebase
@api_view(['POST'])
def verify_token(request):
    token = request.data.get('token')
    if not token:
        return JsonResponse({"message": "Token no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        uid = decoded_token.get('uid')

        # Aquí puedes buscar o crear un usuario en tu base de datos
        # user, created = User.objects.get_or_create(firebase_uid=uid)
        
        return JsonResponse({"message": "Token válido", "uid": uid}, status=status.HTTP_200_OK)
    except firebase_auth.InvalidIdTokenError:
        return JsonResponse({"message": "Token inválido"}, status=status.HTTP_401_UNAUTHORIZED)
    except firebase_auth.ExpiredIdTokenError:
        return JsonResponse({"message": "Token expirado"}, status=status.HTTP_401_UNAUTHORIZED)
    except firebase_auth.RevokedIdTokenError:
        return JsonResponse({"message": "Token revocado"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return JsonResponse({"message": "Error en la verificación del token"}, status=status.HTTP_400_BAD_REQUEST)

# Viewset para Species
class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

# Viewset para Observation
class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
