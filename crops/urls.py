from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CropViewSet, CropCategoryViewSet

router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'categories', CropCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
