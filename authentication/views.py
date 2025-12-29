from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LogoutSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.

    Allows any user (authenticated or not) to create a new account.
    """

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(generics.GenericAPIView):
    """
    API endpoint for user logout.

    Accepts a refresh token and adds it to the blacklist,
    effectively invalidating the session.
    """

    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """
        Blacklists the provided refresh token.

        Args:
            request: The HTTP request containing the 'refresh' token.

        Returns:
            205 RESET CONTENT on success, or 400 BAD REQUEST on failure.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = serializer.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
