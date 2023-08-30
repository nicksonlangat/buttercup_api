
from django.db import transaction

from common.services import model_update

from .models import Category, Flower

def category_create(*, name: str) -> Category:
    obj = Category(name=name)

    obj.full_clean()
    obj.save()

    return obj

@transaction.atomic
def category_update(*, category: Category, data) -> Category:
    non_side_effect_fields = []

    category, has_updated = model_update(instance=category, fields=non_side_effect_fields, data=data)

    return category


class FlowerService:
     def __init__(self, flower: Flower):
        self.flower = flower

     @transaction.atomic
     def create(self, category, name, description, image, price, available) -> Flower:

        obj = Flower(
            category_id=category.id,
            name=name,
            description=description,
            image=image,
            price=price,
            available=available
        )

        obj.full_clean()
        obj.save()

        return obj
     
     @transaction.atomic
     def update(*, flower: Flower, data) -> Flower:
        non_side_effect_fields = []

        flower, has_updated = model_update(instance=flower, fields=non_side_effect_fields, data=data)

        return flower


def flower_create(*, category, name, description, image, price, available) -> Flower:
        obj = Flower(
            category=category,
            name=name,
            description=description,
            image=image,
            price=price,
            available=available
        )

        obj.full_clean()
        obj.save()

        return obj
