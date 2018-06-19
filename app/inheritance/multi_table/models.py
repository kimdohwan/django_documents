from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.pk}]Place({self.name})'

    class Meta:
        ordering = ['name']


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} Restaurant'


class Supplier(Place):
    customers = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='supplier_by_customer'
    )


# 멀티테이블은 어지간하면 안쓰는게 좋다
# 한단계가 넘어가면 성능이 매우 떨어진다고 한다