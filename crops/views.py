from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Crop, CropCategory
from .serializers import CropSerializer, CropCategorySerializer


class CropCategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing crop categories.

    Provides standard CRUD operations:
    - List all categories
    - Create a new category
    - Retrieve, update, or delete a specific category
    """
    queryset = CropCategory.objects.all()
    serializer_class = CropCategorySerializer
    permission_classes = [IsAuthenticated]


class CropViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing crops.

    Features:
    - Full CRUD operations.
    - Filtering by 'category' and 'water_requirements'.
    - Search by 'name' and 'scientific_name'.
    - Ordering by 'name', 'created_at', and 'growth_duration_days'.
    - Pagination is enabled globally.
    """
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'water_requirements']
    search_fields = ['name', 'scientific_name']
    ordering_fields = ['name', 'created_at', 'growth_duration_days']
