from rest_framework import serializers

from .models import Crop, CropCategory


class CropCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the CropCategory model.

    Converts category instances into JSON format and validates input data
    for creating or updating categories.
    """

    class Meta:
        model = CropCategory
        fields = "__all__"


class CropSerializer(serializers.ModelSerializer):
    """
    Serializer for the Crop model.

    Features:
    - **Read Operations (GET):** Includes a nested 'category_details' field
      that provides the full category object (name, description, etc.),
      not just the ID.
    - **Write Operations (POST/PUT):** Uses the standard 'category' field
      which expects a Category ID.
    """

    category_details = CropCategorySerializer(source="category", read_only=True)

    class Meta:
        model = Crop
        fields = [
            "id",
            "name",
            "scientific_name",
            "category",
            "category_details",
            "description",
            "growth_duration_days",
            "water_requirements",
            "created_at",
            "updated_at",
        ]
