import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_register_user(client):
    payload = {"username": "new", "password": "pwd", "email": "a@a.com"}
    response = client.post('/api/auth/register/', payload)
    assert response.status_code == 201
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_login_user(client, user):
    payload = {"username": "testuser", "password": "password123"}
    response = client.post('/api/auth/login/', payload)
    assert response.status_code == 200
    assert "access" in response.data
