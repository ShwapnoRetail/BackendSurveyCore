from rest_framework import permissions

class IsJWTAuthenticated(permissions.BasePermission):
    """
    Custom permission for JWT-authenticated users from central auth
    """
    def has_permission(self, request, view):
        # Our authentication class provides user dict if valid
        return bool(request.user and 'user_id' in request.user)