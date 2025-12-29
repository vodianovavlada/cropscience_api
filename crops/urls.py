from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CropCategoryViewSet, CropViewSet

router = DefaultRouter()
router.register(r"crops", CropViewSet)
router.register(r"categories", CropCategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
