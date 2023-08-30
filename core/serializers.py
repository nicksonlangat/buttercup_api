from rest_framework import serializers

from .models import Category, Flower

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = [
            "id", "category", "name", 
            "description", "image",
            "price", "available",
            "created_at", "updated_at"
            ]
