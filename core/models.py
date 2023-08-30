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
