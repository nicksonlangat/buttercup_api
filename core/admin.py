from django.contrib import admin
from .models import Category, Flower, Order, OrderItem
# Register your models here.
admin.site.register(Category)
admin.site.register(Flower)
admin.site.register(Order)
admin.site.register(OrderItem)
