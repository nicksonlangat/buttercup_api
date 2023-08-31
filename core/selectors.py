from django.db.models.query import QuerySet

from .filters import (
    BaseCategoryFilter,
    BaseFlowerFilter,
    BaseOrderFilter,
    BaseOrderItemFilter
)
from .models import (
    Category, Flower, Order, OrderItem
)

def category_list(*, filters=None) -> QuerySet[Category]:
    filters = filters or {}

    qs = Category.objects.all()

    return BaseCategoryFilter(filters, qs).qs


def flower_list(*, filters=None) -> QuerySet[Category]:
    filters = filters or {}

    qs = Flower.objects.all()

    return BaseFlowerFilter(filters, qs).qs


def order_list(*, filters=None) -> QuerySet[Order]:
    filters = filters or {}

    qs = Order.objects.all()

    return BaseOrderFilter(filters, qs).qs


def order_item_list(*, filters=None) -> QuerySet[Order]:
    filters = filters or {}

    qs = OrderItem.objects.all()

    return BaseOrderItemFilter(filters, qs).qs
