from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse

class TokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Process incoming requests to validate JWT tokens in the Authorization header.
        """
        auth_header = request.headers.get('Authorization')

        # Check if the Authorization header exists and starts with "Bearer"
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                # Validate the token
                validated_token = JWTAuthentication().get_validated_token(token)
                user = JWTAuthentication().get_user(validated_token)
                request.user = user  # Attach the authenticated user to the request
            except AuthenticationFailed as e:
                # Return a 401 Unauthorized response for invalid/expired tokens
                return JsonResponse(
                    {"error": "Invalid or expired token.", "details": str(e)},
                    status=401
                )
        else:
            # Handle missing Authorization header
            if request.path.startswith('/api/'):  # Customize for specific API paths
                return JsonResponse(
                    {"error": "Authorization header missing or invalid format."},
                    status=401
                )
        # Proceed to the next middleware or view
        return None
