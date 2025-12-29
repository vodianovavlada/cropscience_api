from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Handles the creation of a new User instance.
    Ensures that the password is:
    1. Marked as write_only (never returned in the API response).
    2. Correctly hashed using create_user() method.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        """
        Creates a new user with an encrypted password.
        """
        return User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
        )


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for the Logout endpoint.

    Validates that a 'refresh' token is provided in the request body.
    This token is required to perform the blacklisting operation.
    """

    refresh = serializers.CharField()
