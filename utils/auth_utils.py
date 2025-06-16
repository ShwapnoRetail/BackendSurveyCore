import requests
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
import jwt
from jwt import ExpiredSignatureError, DecodeError


def validate_shwapno_jwt(token):
    """
    Validate JWT token from Shwapno central auth
    Returns: {
        'user_id': int,
        'is_admin': bool,
        'username': str,
        'email': str
    }
    """
    try:
        # Skip verification since we trust the central auth
        payload = jwt.decode(token, options={"verify_signature": False})

        # Verify user data structure
        if not payload.get('user_id'):
            raise AuthenticationFailed('Invalid token payload')

        return {
            'user_id': payload['user_id'],
            'username': payload.get('username', ''),
            'email': payload.get('email', ''),
            'is_admin': 'admin' in payload.get('access_info', [])
        }

    except ExpiredSignatureError:
        raise AuthenticationFailed('Token expired')
    except DecodeError:
        raise AuthenticationFailed('Invalid token')
    except Exception as e:
        raise AuthenticationFailed(f'Token validation failed: {str(e)}')