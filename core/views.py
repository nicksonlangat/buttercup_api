
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import LimitOffsetPagination, get_paginated_response

from .models import Category
from .serializers import CategorySerializer, FlowerSerializer
from .services import Cart, category_create, category_update, flower_create
from .selectors import category_list, flower_list


class CategoryCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows categories to be created
    """

    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        category_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class CategoryListApi(generics.ListAPIView):
    """
    API endpoint that lists all categories
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 25
    
    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = category_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=CategorySerializer,
            queryset=qs,
            request=request,
            view=self,
        )


class CategoryUpdateApi(generics.RetrieveUpdateAPIView):
    """
    API endpoint that updates a category
    """

    queryset = category_list()
    serializer_class = CategorySerializer

    def patch(self, request, pk, format=None):  
        category = self.queryset.objects.get(id=pk)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            category_update(category, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteApi(generics.DestroyAPIView):
    """
    API endpoint that deletes a category
    """

    def delete(self, request, pk, format=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlowerCreateApi(generics.CreateAPIView):
    """
    API endpoint that allows products to be created
    """

    serializer_class = FlowerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        flower_create(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FlowerListApi(generics.ListAPIView):
    """
    API endpoint that lists all flowers
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 25
    
    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = flower_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=FlowerSerializer,
            queryset=qs,
            request=request,
            view=self,
        )


class CartAPI(APIView):
    """
    Single API to handle cart operations
    """
    def get(self, request, format=None):
        cart = Cart(request)

        return Response(
            {"cart": list(cart.__iter__()), 
            "cart_total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )
    
    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

        elif "clear" in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(
                    product=product["product"],
                    quantity=product["quantity"],
                    overide_quantity=product["overide_quantity"] if "overide_quantity" in product else False
                )
        
        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED)

