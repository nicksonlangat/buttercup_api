import random
import string
from django.db import models
from common.models import BaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)


class Flower(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='flowers', blank=True, null=True)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='flowers', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)


class Order(BaseModel):
   order_number = models.CharField(max_length=250, blank=True, null=True)
   full_name = models.CharField(max_length=250)
   email = models.EmailField(blank=True, null=True)
   phone_number = models.CharField(max_length=15)
   address = models.CharField(max_length=250)
   card_number = models.CharField(max_length=250)
   card_expiry = models.CharField(max_length=250)
   card_cvc = models.CharField(max_length=250)
   is_paid = models.BooleanField(default=False)

   def save(self, *args, **kwargs):
        if not self.order_number:
            chars=string.ascii_uppercase + string.digits
            self.order_number = ''.join(random.choice(chars) for _ in range(6))
        super(Order, self).save(*args, **kwargs)


   def __str__(self) -> str:
       return str(self.order_number)
   
   def get_total_cost(self):
       return sum(item.get_cost() for item in self.items.all())
   

class OrderItem(BaseModel):
   order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
   flower = models.ForeignKey(Flower, related_name='order_items', on_delete=models.CASCADE)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   quantity = models.PositiveIntegerField(default=1)

   def __str__(self) -> str:
       return str(self.id)
   
   def get_cost(self):
       return self.price * self.quantity
