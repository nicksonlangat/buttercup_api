from django.urls import path

from .views import (
    CategoryCreateApi,
    CategoryListApi,
    CategoryUpdateApi,
    CategoryDeleteApi,
    FlowerCreateApi,
    FlowerListApi,
    CartAPI
    )

urlpatterns = [
    # category endpoints
    path("categories/create/", CategoryCreateApi.as_view(), name="category_create"),
    path("categories/list/", CategoryListApi.as_view(), name="category_list"),
    path("categories/update/<uuid:pk>/", CategoryUpdateApi.as_view(), name="category_update"),
    path("categories/delete/<uuid:pk>/", CategoryDeleteApi.as_view(), name="category_delete"),

    # flower endpoints
    path("flowers/create/", FlowerCreateApi.as_view(), name="flower_create"),
    path("flowers/list/", FlowerListApi.as_view(), name="flower_list"),

    # cart endpoints
    path("cart/", CartAPI.as_view(), name="cart"),
]
