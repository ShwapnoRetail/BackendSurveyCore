from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from .auth_utils import validate_shwapno_jwt


class ShwapnoJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]
        try:
            user_data = validate_shwapno_jwt(token)
            # Return the user data as the user object
            return (user_data, None)
        except AuthenticationFailed as e:
            raise AuthenticationFailed(str(e))