from django.urls import path

from .views import (
    CategoryApi,
    FlowerApi,
    CartAPI,
    OrderApi,
    OrderItemApi
    )

urlpatterns = [
    # category endpoints
    path("categories/", CategoryApi.as_view(), name="categories"),

    # flower endpoints
    path("flowers/", FlowerApi.as_view(), name="flowers"),

    # cart endpoints
    path("cart/", CartAPI.as_view(), name="cart"),

    # order endpoints
    path("orders/", OrderApi.as_view(), name="orders"),

    # order item endpoints
    path("order/items", OrderItemApi.as_view(), name="order_items"),
]
