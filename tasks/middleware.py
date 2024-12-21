from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken

class TokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the authenticated user
            user = request.user
            # Generate a new refresh token for the user
            refresh = RefreshToken.for_user(user)
            # Get the access token from the refresh token
            access_token = str(refresh.access_token)
            # Add the access token to the request headers
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
            print(f"Token added to request: {access_token}")  # Debug statement
        else:
            print("User is not authenticated")  # Debug statement