import django_filters
from .models import Category, Flower

class BaseCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ("id", "name")


class BaseFlowerFilter(django_filters.FilterSet):
    class Meta:
        model = Flower
        fields = ( 
            "id", "name", "available",
        )
