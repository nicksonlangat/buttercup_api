from django.db.models.query import QuerySet

from .filters import (
    BaseCategoryFilter,
    BaseFlowerFilter
)
from .models import (
    Category, Flower
)

def category_list(*, filters=None) -> QuerySet[Category]:
    filters = filters or {}

    qs = Category.objects.all()

    return BaseCategoryFilter(filters, qs).qs


def flower_list(*, filters=None) -> QuerySet[Category]:
    filters = filters or {}

    qs = Flower.objects.all()

    return BaseFlowerFilter(filters, qs).qs
