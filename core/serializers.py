from rest_framework import serializers

from .models import Category, Flower, Order, OrderItem

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
    def to_representation(self, instance):
            data = super(FlowerSerializer, self).to_representation(instance)
            data["category"] = CategorySerializer(Category.objects.get(id=instance.category.id)).data
            return data


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id", "order_number", "full_name", "phone_number",
            "address", "card_number", "card_expiry", "is_paid",
            "email", "card_cvc", "created_at", "updated_at"
            ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "id", "order", "flower", "quantity",
             "created_at", "updated_at"
            ]
        
    def to_representation(self, instance):
            data = super(OrderItemSerializer, self).to_representation(instance)
            data["order"] = OrderSerializer(Order.objects.get(id=instance.order.id)).data
            data["flower"] = FlowerSerializer(Flower.objects.get(id=instance.flower.id)).data
            return data
