from rest_framework import serializers
from .models import Crop, CropCategory


class CropCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCategory
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    category_details = CropCategorySerializer(source='category', read_only=True)

    class Meta:
        model = Crop
        fields = [
            'id', 'name', 'scientific_name', 'category', 'category_details',
            'description', 'growth_duration_days', 'water_requirements',
            'created_at', 'updated_at'
        ]
        