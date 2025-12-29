import pytest
from crops.models import Crop


@pytest.mark.django_db
def test_get_crops_unauthorized(client):
    response = client.get('/api/crops/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_crop(auth_client, category):
    payload = {
        "name": "Test Wheat",
        "scientific_name": "Triticum",
        "category": category.id,
        "growth_duration_days": 100,
        "water_requirements": "medium"
    }

    response = auth_client.post('/api/crops/', payload)

    assert response.status_code == 201
    assert Crop.objects.count() == 1
    assert response.data['name'] == "Test Wheat"


@pytest.mark.django_db
def test_get_crops_list(auth_client, category):
    Crop.objects.create(name="Crop 1", scientific_name="A", category=category, growth_duration_days=10,
                        water_requirements="low")
    Crop.objects.create(name="Crop 2", scientific_name="B", category=category, growth_duration_days=20,
                        water_requirements="high")

    response = auth_client.get('/api/crops/')

    assert response.status_code == 200
    assert response.data['count'] == 2


@pytest.mark.django_db
def test_filter_crops(auth_client, category):
    Crop.objects.create(name="Cactus", scientific_name="C", category=category, growth_duration_days=10,
                        water_requirements="low")
    Crop.objects.create(name="Rice", scientific_name="R", category=category, growth_duration_days=10,
                        water_requirements="high")

    response = auth_client.get('/api/crops/?water_requirements=low')

    assert response.status_code == 200
    assert response.data['count'] == 1
    assert response.data['results'][0]['name'] == "Cactus"