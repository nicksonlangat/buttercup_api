import django_filters
from .models import Category, Flower, Order, OrderItem

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


class BaseOrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ( 
            "id", "is_paid", "order_number"
        )

class BaseOrderItemFilter(django_filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = ( 
            "id", "order"
        )
