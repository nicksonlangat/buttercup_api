
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.pagination import (
    LimitOffsetPagination, get_paginated_response
)

from .models import Category
from .serializers import (
    CategorySerializer, FlowerSerializer,
      OrderItemSerializer, OrderSerializer
)
from .services import (
    Cart, category_create,
    category_update, flower_create, 
    order_item_create
)
from .selectors import (
    category_list, flower_list, 
    order_item_list, order_list
)


class CategoryApi(
    generics.CreateAPIView, generics.ListAPIView, 
    generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    API for category operations
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 25

    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        category_create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

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

    def patch(self, request, pk, format=None):  
        category = category_list().objects.get(id=pk)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            category_update(category, data=serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlowerApi(generics.CreateAPIView, generics.ListAPIView):
    """
    API for product operations
    """

    class Pagination(LimitOffsetPagination):
        default_limit = 25

    serializer_class = FlowerSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        flower_create(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
    API for cart operations
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


class OrderApi(generics.CreateAPIView, generics.ListAPIView):
    """
    API for order operations
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 25

    serializer_class = OrderSerializer
    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order_item_create(order, list(cart.__iter__()))
        cart.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = order_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=OrderSerializer,
            queryset=qs,
            request=request,
            view=self,
        )


class OrderItemApi(generics.ListAPIView):
    """
    API endpoint that for order item operations
    """
    class Pagination(LimitOffsetPagination):
        default_limit = 25

    serializer_class = OrderItemSerializer

    def get(self, request, *args, **kwargs):
        filters = request.query_params
        qs = order_item_list(filters=filters)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=OrderItemSerializer,
            queryset=qs,
            request=request,
            view=self,
        )
