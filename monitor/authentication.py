from firebase_admin import auth
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        id_token = auth_header.split(' ').pop()
        try:
            # Verifica el token con Firebase
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token.get('uid')

            # Intenta obtener el usuario de la base de datos
            try:
                user = User.objects.get(username=uid)
            except User.DoesNotExist:
                # Si el usuario no existe, puedes crearlo o lanzar un error
                user = User.objects.create(username=uid)
                # Aquí podrías agregar más información al usuario si es necesario

            return (user, None)
        except auth.InvalidIdTokenError:
            raise AuthenticationFailed('Token inválido')
        except auth.ExpiredIdTokenError:
            raise AuthenticationFailed('Token expirado')
        except auth.RevokedIdTokenError:
            raise AuthenticationFailed('Token revocado')
        except Exception as e:
            raise AuthenticationFailed(f'Error en la autenticación: {str(e)}')

        return None
