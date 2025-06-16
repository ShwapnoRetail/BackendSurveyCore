import jwt
from rest_framework.exceptions import AuthenticationFailed


def validate_shwapno_jwt(token):
    try:
        # Skip signature verification since we trust the central auth
        payload = jwt.decode(token, options={"verify_signature": False})

        # Verify essential claims
        if not payload.get('user_id'):
            raise AuthenticationFailed('Invalid token payload')

        return {
            'user_id': payload['user_id'],
            'username': payload.get('username', ''),
            'email': payload.get('email', ''),
            'is_admin': 'admin' in payload.get('access_info', [])
        }

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.DecodeError:
        raise AuthenticationFailed('Invalid token format')
    except Exception as e:
        raise AuthenticationFailed(f'Token validation error: {str(e)}')

