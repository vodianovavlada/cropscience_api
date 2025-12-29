import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from crops.models import CropCategory


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="password123")


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def category():
    return CropCategory.objects.create(name="Test Category")
