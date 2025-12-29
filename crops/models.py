from django.db import models


class CropCategory(models.Model):
    """
    Represents a category of crops (e.g., Cereals, Vegetables).

    Attributes:
        name (str): Unique name of the category.
        description (str): Optional detailed description.
        created_at (datetime): Timestamp when the category was created.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the string representation of the category."""
        return self.name


class Crop(models.Model):
    """
    Represents a specific crop variety with its agricultural characteristics.

    Attributes:
        name (str): Common name of the crop.
        scientific_name (str): Latin scientific name.
        category (CropCategory): Foreign key to the related category.
        description (str): Optional description.
        growth_duration_days (int): Average days from planting to harvest.
        water_requirements (str): Water needs level (low, medium, high).
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of the last update.
    """
    WATER_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150)
    category = models.ForeignKey(CropCategory, on_delete=models.CASCADE, related_name='crops')
    description = models.TextField(blank=True, null=True)
    growth_duration_days = models.IntegerField()
    water_requirements = models.CharField(max_length=10, choices=WATER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['scientific_name']),
        ]

    def __str__(self):
        """Returns the string representation of the crop."""
        return self.name